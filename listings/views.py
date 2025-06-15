"""
Views for the listings app.

This module contains the API views for travel listings and amenities.
"""

from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import QuerySet
from typing import Any
from .models import Listing, Amenity, Booking, Review
from .serializers import (
    ListingSerializer,
    AmenitySerializer,
    BookingSerializer,
    ReviewSerializer,
)


class ListingViewSet(viewsets.ModelViewSet):
    """
    API endpoint for travel listings
    """

    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    lookup_field = "slug"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = [
        "listing_type",
        "is_available",
        "location",
        "max_guests",
        "bedrooms",
    ]
    search_fields = ["title", "description", "location", "address"]
    ordering_fields = ["price_per_night", "created_at", "bedrooms", "max_guests"]

    @action(detail=False)
    def featured(self, request):
        """Get featured listings"""
        featured = self.get_queryset().filter(is_available=True)[:5]
        serializer = self.get_serializer(featured, many=True)
        return Response(serializer.data)


class AmenityViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for amenities
    """

    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BookingViewSet(viewsets.ModelViewSet):
    """
    API endpoint for bookings
    """

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]
    filterset_fields = [
        "listing",
        "status",
        "check_in_date",
        "check_out_date",
        "user",
    ]
    ordering_fields = ["created_at", "check_in_date", "total_price"]
    ordering = ["-created_at"]

    def get_queryset(self) -> QuerySet[Booking]:  # type: ignore
        """Filter bookings by user for non-staff users"""
        if self.request.user.is_staff:
            return Booking.objects.all()
        return Booking.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Set the user to the current user when creating a booking"""
        serializer.save(user=self.request.user)

    @action(detail=False, methods=["get"])
    def my_bookings(self, request):
        """Get current user's bookings"""
        bookings = Booking.objects.filter(user=request.user)
        serializer = self.get_serializer(bookings, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def upcoming(self, request):
        """Get upcoming bookings for current user"""
        from datetime import date

        upcoming_bookings = Booking.objects.filter(
            user=request.user,
            check_in_date__gte=date.today(),
            status__in=["pending", "confirmed"],
        )
        serializer = self.get_serializer(upcoming_bookings, many=True)
        return Response(serializer.data)


class ReviewViewSet(viewsets.ModelViewSet):
    """
    API endpoint for reviews
    """

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]
    filterset_fields = [
        "listing",
        "user",
        "rating",
    ]
    ordering_fields = ["created_at", "rating"]
    ordering = ["-created_at"]

    def get_queryset(self) -> QuerySet[Review]:  # type: ignore
        """Filter reviews and allow users to edit only their own reviews"""
        queryset = Review.objects.all()

        # Filter by listing_id if specified in query params
        listing_id = getattr(self.request, "query_params", self.request.GET).get(  # type: ignore
            "listing_id", None
        )
        if listing_id is not None:
            queryset = queryset.filter(listing_id=listing_id)

        # For update/delete operations, non-staff users can only access their own reviews
        if self.action in ["update", "partial_update", "destroy"]:
            if not self.request.user.is_staff:
                queryset = queryset.filter(user=self.request.user)

        return queryset

    def perform_create(self, serializer):
        """Set the user to the current user when creating a review"""
        serializer.save(user=self.request.user)

    @action(detail=False, methods=["get"])
    def my_reviews(self, request):
        """Get current user's reviews"""
        reviews = Review.objects.filter(user=request.user)
        serializer = self.get_serializer(reviews, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def top_rated(self, request):
        """Get top rated reviews (5 stars)"""
        top_reviews = Review.objects.filter(rating=5)[:10]
        serializer = self.get_serializer(top_reviews, many=True)
        return Response(serializer.data)
