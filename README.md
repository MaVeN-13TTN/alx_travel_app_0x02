# 🏨 ALX Travel App - Milestone 2

A **production-ready Django REST API** for a travel listing platform with comprehensive database modeling, API serialization, and data seeding capabilities. This project demonstrates industry best practices for Django development, including proper model relationships, serializers, and management commands.

[![Django Version](https://img.shields.io/badge/Django-5.2.1-green.svg)](https://djangoproject.com/)
[![Python Version](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🎯 Milestone 2 Achievements

This project successfully implements **Milestone 2: Database Modeling and Data Seeding** with the following core features:

### ✅ **Database Models (Complete)**

- **Listing Model**: Travel accommodations with comprehensive fields and relationships
- **Booking Model**: User bookings with foreign key relationships to User and Listing
- **Review Model**: User reviews with ratings, linked to both User and Listing
- **Supporting Models**: Amenity, ListingImage, ListingAmenity for rich data representation

### ✅ **API Serializers (Complete)**

- **ListingSerializer**: Full CRUD serialization with nested relationships
- **BookingSerializer**: Booking management with read/write field separation
- **ReviewSerializer**: Review handling with proper validation
- **Supporting Serializers**: AmenitySerializer, ListingImageSerializer

### ✅ **Data Seeding (Complete)**

- **Management Command**: Custom Django command for database population
- **Sample Data**: Realistic travel listings, bookings, and reviews
- **Relationship Integrity**: Proper foreign key relationships maintained
- **Configurable**: Command-line arguments for different data volumes

## 🚀 Key Features

- **🏠 Listings Management**: Complete CRUD operations for travel accommodations (hotels, apartments, villas, resorts, hostels)
- **� Booking System**: Full booking lifecycle with status tracking (pending, confirmed, cancelled, completed)
- **⭐ Review System**: User reviews with 1-5 star ratings and comments
- **�🔧 REST API**: Built with Django REST Framework with nested serializers
- **📖 API Documentation**: Automatic Swagger/OpenAPI documentation with drf-yasg
- **🔒 Security**: Secure environment variable management with django-environ
- **🗄️ Database**: MySQL integration with optimized model relationships
- **⚡ Background Tasks**: Celery with RabbitMQ for asynchronous processing
- **🌐 CORS**: Cross-Origin Resource Sharing for frontend integration
- **� Data Seeding**: One-command database population with realistic sample data

## 📊 Database Schema

### Core Models

| Model            | Purpose               | Key Relationships                                    |
| ---------------- | --------------------- | ---------------------------------------------------- |
| **Listing**      | Travel accommodations | → ListingImage (1:many), → Amenity (many:many)       |
| **Booking**      | User reservations     | → User (many:1), → Listing (many:1)                  |
| **Review**       | User feedback         | → User (many:1), → Listing (many:1), → Booking (1:1) |
| **Amenity**      | Property features     | → Listing (many:many)                                |
| **ListingImage** | Property photos       | → Listing (many:1)                                   |

### Sample Data Included

- **10 Amenities**: WiFi, Swimming Pool, Parking, Air Conditioning, Kitchen, Gym, Pet Friendly, Balcony, Beach Access, Room Service
- **5 Test Users**: Realistic user profiles for testing
- **10 Diverse Listings**: Various accommodation types across different locations
- **20 Bookings**: Realistic booking scenarios with proper date ranges
- **15 Reviews**: User reviews with ratings and detailed comments

## 🛠️ Tech Stack

| Category           | Technology            | Version |
| ------------------ | --------------------- | ------- |
| **Backend**        | Django                | 5.2.1   |
| **API**            | Django REST Framework | 3.16.0  |
| **Database**       | MySQL                 | 8.0+    |
| **Documentation**  | drf-yasg              | 1.21.10 |
| **Task Queue**     | Celery                | 5.5.2   |
| **Message Broker** | RabbitMQ/Pika         | 1.3.2   |
| **Environment**    | django-environ        | 0.12.0  |
| **CORS**           | django-cors-headers   | 4.7.0   |
| **Images**         | Pillow                | 11.2.1  |

## 📋 Prerequisites

- **Python 3.12+**
- **MySQL 8.0+**
- **RabbitMQ** (optional, for background tasks)
- **Git** (for version control)

## ⚡ Quick Start

### 1. Clone & Setup

```bash
# Clone the repository
git clone https://github.com/MaVeN-13TTN/alx_travel_app_0x00.git
cd alx_travel_app_0x00

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Environment Configuration

```bash
# Copy environment template
cp .env.example .env

# Generate a secure SECRET_KEY
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# Edit .env file with your settings
nano .env
```

**Required Environment Variables:**

```bash
# Security
SECRET_KEY=your-generated-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Configuration
# Replace these with your actual database credentials
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=3306

# CORS (for frontend integration)
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
```

### 3. Database Setup

Create the MySQL database and user (replace with your actual values):

```sql
-- Connect to MySQL as root
mysql -u root -p

-- Create database and user (replace with your chosen names)
CREATE DATABASE your_database_name;
CREATE USER 'your_database_user'@'localhost' IDENTIFIED BY 'your_secure_password';
GRANT ALL PRIVILEGES ON your_database_name.* TO 'your_database_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

**Note:** Make sure your password meets MySQL's security requirements (uppercase, lowercase, numbers, and special characters).

### 4. Django Setup & Database Migration

```bash
# Run migrations to create all tables
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser

# Populate database with sample data (Milestone 2 Feature)
python manage.py seed

# Optional: Customize seed data volumes
python manage.py seed --listings 20 --bookings 50 --reviews 30

# Start development server
python manage.py runserver
```

## 🌱 Data Seeding (Milestone 2 Feature)

The project includes a powerful management command for populating the database with realistic sample data. This is perfect for development, testing, and demonstration purposes.

### Seed Command Usage

```bash
# Basic seeding with default values
python manage.py seed

# Custom data volumes
python manage.py seed --listings 15 --bookings 40 --reviews 25

# Help and options
python manage.py seed --help
```

### What Gets Created

| Data Type     | Default Count | Description                                                                                                     |
| ------------- | ------------- | --------------------------------------------------------------------------------------------------------------- |
| **Amenities** | 10            | WiFi, Swimming Pool, Parking, Air Conditioning, Kitchen, Gym, Pet Friendly, Balcony, Beach Access, Room Service |
| **Users**     | 5             | Test users with realistic profiles (john_doe, jane_smith, bob_wilson, alice_brown, charlie_davis)               |
| **Listings**  | 10            | Diverse accommodations across different cities and types                                                        |
| **Bookings**  | 20            | Realistic booking scenarios with proper date ranges and pricing                                                 |
| **Reviews**   | 15            | User reviews with 3-5 star ratings and detailed comments                                                        |

### Sample Data Examples

**Listings Include:**

- Luxury Beachfront Villa (Malibu, CA) - $450/night
- Cozy Downtown Apartment (New York, NY) - $120/night
- Mountain Resort Cabin (Aspen, CO) - $200/night
- Boutique Hotel Suite (San Francisco, CA) - $300/night
- Budget-Friendly Hostel (Portland, OR) - $35/night

**Relationships Maintained:**

- ✅ Users have multiple bookings and reviews
- ✅ Listings have associated amenities and images
- ✅ Bookings calculate realistic total prices
- ✅ Reviews are linked to both users and listings
- ✅ All foreign key constraints respected

### 5. Access the Application

| Interface          | URL                            | Description                   |
| ------------------ | ------------------------------ | ----------------------------- |
| **🔧 Admin Panel** | http://127.0.0.1:8000/admin/   | Django admin interface        |
| **📖 Swagger UI**  | http://127.0.0.1:8000/swagger/ | Interactive API documentation |
| **📋 ReDoc**       | http://127.0.0.1:8000/redoc/   | Alternative API documentation |
| **🔗 API Root**    | http://127.0.0.1:8000/api/     | REST API endpoints            |

## 📁 Project Structure

```
alx_travel_app/                     # 📦 Project root
├── 📄 README.md                    # Project documentation
├── 📄 SECURITY.md                  # Security guidelines
├── 📄 requirements.txt             # Python dependencies
├── 🔒 .env                         # Environment variables (not in VCS)
├── 📋 .env.example                 # Environment template
├── 🚫 .gitignore                   # Git ignore rules
├── ⚙️ manage.py                    # Django management script
├── 📁 alx_travel_app/              # Django project package
│   ├── ⚙️ settings.py              # Django settings
│   ├── 🌐 urls.py                  # Main URL configuration
│   ├── 🔧 wsgi.py                  # WSGI configuration
│   ├── ⚡ asgi.py                  # ASGI configuration
│   └── 🔄 celery_app.py            # Celery configuration
├── 📁 listings/                    # Listings app
│   ├── 🗄️ models.py               # Database models
│   ├── 🔧 views.py                 # API views
│   ├── 📝 serializers.py           # DRF serializers
│   ├── 🌐 urls.py                  # App URLs
│   ├── ⚙️ admin.py                 # Admin configuration
│   └── 📁 migrations/              # Database migrations
├── 📁 static/                      # Static files
├── 📁 media/                       # Uploaded files
└── 📁 templates/                   # HTML templates
```

## 🔗 API Endpoints (Milestone 2)

### Core Models API

| Model         | Endpoint Base     | Description               |
| ------------- | ----------------- | ------------------------- |
| **Listings**  | `/api/listings/`  | Travel accommodations     |
| **Bookings**  | `/api/bookings/`  | User reservations         |
| **Review**    | `/api/reviews/`   | User feedback and ratings |
| **Amenities** | `/api/amenities/` | Property features         |

### 🏠 Listings API

| Method   | Endpoint              | Description                      |
| -------- | --------------------- | -------------------------------- |
| `GET`    | `/api/listings/`      | List all listings with filtering |
| `POST`   | `/api/listings/`      | Create new listing               |
| `GET`    | `/api/listings/{id}/` | Retrieve specific listing        |
| `PUT`    | `/api/listings/{id}/` | Update listing                   |
| `PATCH`  | `/api/listings/{id}/` | Partial update listing           |
| `DELETE` | `/api/listings/{id}/` | Delete listing                   |

**Listing Fields:**

```json
{
  "id": 1,
  "title": "Luxury Beachfront Villa",
  "slug": "luxury-beachfront-villa",
  "description": "Beautiful villa with stunning ocean views...",
  "listing_type": "villa",
  "price_per_night": "450.00",
  "location": "Malibu, California",
  "address": "123 Ocean Drive, Malibu, CA 90265",
  "max_guests": 8,
  "bedrooms": 4,
  "bathrooms": 3,
  "featured_image": "/media/listings/2024/06/villa.jpg",
  "is_available": true,
  "created_at": "2024-06-12T10:30:00Z",
  "updated_at": "2024-06-12T10:30:00Z",
  "images": [...],
  "amenities": [...]
}
```

### 📅 Bookings API

| Method   | Endpoint              | Description               |
| -------- | --------------------- | ------------------------- |
| `GET`    | `/api/bookings/`      | List user's bookings      |
| `POST`   | `/api/bookings/`      | Create new booking        |
| `GET`    | `/api/bookings/{id}/` | Retrieve specific booking |
| `PUT`    | `/api/bookings/{id}/` | Update booking            |
| `PATCH`  | `/api/bookings/{id}/` | Partial update booking    |
| `DELETE` | `/api/bookings/{id}/` | Cancel booking            |

**Booking Fields:**

```json
{
  "id": 1,
  "user": "john_doe",
  "listing": {...},
  "listing_id": 1,
  "check_in_date": "2024-07-15",
  "check_out_date": "2024-07-20",
  "num_guests": 4,
  "total_price": "2250.00",
  "status": "confirmed",
  "created_at": "2024-06-12T10:30:00Z",
  "updated_at": "2024-06-12T10:30:00Z"
}
```

### ⭐ Reviews API

| Method   | Endpoint             | Description                 |
| -------- | -------------------- | --------------------------- |
| `GET`    | `/api/reviews/`      | List reviews with filtering |
| `POST`   | `/api/reviews/`      | Create new review           |
| `GET`    | `/api/reviews/{id}/` | Retrieve specific review    |
| `PUT`    | `/api/reviews/{id}/` | Update review               |
| `PATCH`  | `/api/reviews/{id}/` | Partial update review       |
| `DELETE` | `/api/reviews/{id}/` | Delete review               |

**Review Fields:**

```json
{
  "id": 1,
  "user": "jane_smith",
  "listing": {...},
  "listing_id": 1,
  "booking": 1,
  "rating": 5,
  "comment": "Amazing place! Had a wonderful time...",
  "created_at": "2024-06-12T10:30:00Z",
  "updated_at": "2024-06-12T10:30:00Z"
}
```

### 🎯 API Features

- **🔍 Filtering**: Filter by type, location, guests, ratings, etc.
- **🔎 Search**: Full-text search across multiple fields
- **📊 Ordering**: Sort by price, date, rating, etc.
- **📄 Pagination**: Efficient data loading with page numbers
- **🔗 Nested Data**: Related objects included in responses
- **✅ Validation**: Comprehensive input validation
- **🔒 Authentication**: User-based access control

## 🧪 Development & Testing

### Management Commands

```bash
# Database operations
python manage.py migrate                    # Apply migrations
python manage.py makemigrations            # Create new migrations
python manage.py showmigrations            # Show migration status

# Data seeding (Milestone 2)
python manage.py seed                       # Seed with default data
python manage.py seed --listings 20        # Custom listing count
python manage.py seed --bookings 50        # Custom booking count
python manage.py seed --reviews 30         # Custom review count

# User management
python manage.py createsuperuser           # Create admin user
python manage.py changepassword <username> # Change user password

# Database inspection
python manage.py dbshell                   # Access database shell
python manage.py shell                     # Django shell

# Development server
python manage.py runserver                 # Start development server
python manage.py runserver 0.0.0.0:8000   # Accessible from network
```

### Running Tests

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test listings

# Run with coverage
pip install coverage
coverage run --source='.' manage.py test
coverage report
coverage html  # Generate HTML coverage report
```

### Development Features

- **🔄 Auto-reload**: Development server automatically reloads on code changes
- **🐛 Debug Mode**: Detailed error pages in development
- **📊 Admin Panel**: Full CRUD operations via Django admin
- **📖 API Docs**: Interactive Swagger UI for API testing
- **🌱 Sample Data**: One-command database population
- **🔍 Shell Access**: Django shell for database queries and testing

## 🚀 Deployment

### Environment Setup

```bash
# Production settings
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

# Database (Production)
DB_NAME=alxtravelapp_prod
DB_USER=prod_user
DB_PASSWORD=secure_password_here
DB_HOST=your_db_host
DB_PORT=3306

# Security
SECRET_KEY=your-super-secure-secret-key-here
CORS_ALLOWED_ORIGINS=https://yourdomain.com
```

### Production Checklist

- [ ] Set `DEBUG=False` in production
- [ ] Configure secure `SECRET_KEY`
- [ ] Set up proper `ALLOWED_HOSTS`
- [ ] Configure production database
- [ ] Set up HTTPS/SSL certificates
- [ ] Configure static file serving
- [ ] Set up backup strategies
- [ ] Configure monitoring and logging

## 📚 Learning Resources

### Milestone 2 Implementation Guide

This project demonstrates:

1. **Model Design**: Proper Django model relationships (ForeignKey, OneToOne, ManyToMany)
2. **Serializer Implementation**: DRF serializers with nested relationships and validation
3. **Management Commands**: Custom Django commands for data operations
4. **Database Migrations**: Proper migration handling and database schema evolution
5. **Sample Data**: Realistic data generation for development and testing

### Key Concepts Covered

- ✅ Django ORM relationships and constraints
- ✅ REST API design with Django REST Framework
- ✅ Database seeding and data management
- ✅ Environment variable management
- ✅ Project structure and organization
- ✅ Documentation and API specifications

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

- **GitHub Issues**: [Report bugs or request features](https://github.com/MaVeN-13TTN/alx_travel_app_0x00/issues)
- **Documentation**: This README and inline code comments
- **API Docs**: Available at `/swagger/` when running the development server

---

**🎯 Milestone 2 Status: ✅ COMPLETE**

All requirements successfully implemented:

- ✅ Database models with proper relationships
- ✅ API serializers for all core models
- ✅ Data seeding management command
- ✅ Sample data generation and testing
- ✅ Comprehensive documentation

Ready for the next phase of development! 🚀
