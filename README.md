# 🏨 ALX Travel App - Milestone 4: Payment Integration

This milestone integrates the Chapa Payment Gateway into the ALX Travel App, enabling secure, seamless transactions for bookings. The implementation includes API endpoints for initiating and verifying payments, asynchronous email notifications, and robust error handling.

[![Django Version](https://img.shields.io/badge/Django-5.2.1-green.svg)](https://djangoproject.com/)
[![Python Version](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://python.org/)
[![DRF Version](https://img.shields.io/badge/DRF-3.16.0-orange.svg)](https://www.django-rest-framework.org/)
[![Chapa](https://img.shields.io/badge/Payment-Chapa-purple)](https://chapa.co/)

---

## 🎯 Milestone 4 Objectives

**Primary Goal**: Integrate the Chapa API to handle all payment processing for bookings, from initiation to verification and confirmation.

### ✅ **Key Features Implemented**

1.  **✅ Chapa API Integration**: Securely process payments using the `chapa-python` library.
2.  **✅ Payment Model**: A dedicated `Payment` model in the database to track transaction status, amount, and reference IDs.
3.  **✅ Payment Initiation Endpoint**: An API endpoint to start a transaction and generate a Chapa checkout URL.
4.  **✅ Payment Verification Webhook**: A webhook to receive and verify payment status updates from Chapa in real-time.
5.  **✅ Asynchronous Email Confirmation**: Celery task to send users a confirmation email upon successful payment without blocking the API response.

---

## 🚀 Payment Workflow

The payment process follows these steps:

1.  **Create a Booking**: A user first creates a booking for a listing via a `POST` request to `/api/bookings/`.
2.  **Initiate Payment**: The user then makes a `POST` request to `/api/bookings/{booking_id}/pay/`.
3.  **Redirect to Chapa**: The API returns a `checkout_url`. The user is redirected to this URL to complete the payment on Chapa's secure page.
4.  **Payment Verification**: Upon completion, Chapa sends a notification to our webhook (`/api/payments/verify/`). The system verifies the transaction status with Chapa.
5.  **Update Status & Send Email**: If the payment was successful, the booking and payment status are updated to `completed`, and a confirmation email is sent to the user.

---

## 📊 API Endpoints for Payment

### **Primary Endpoints**

| Method | Endpoint                       | Description                     | Authentication |
| :--- | :----------------------------- | :------------------------------ | :--- |
| `POST` | `/api/bookings/{booking_id}/pay/` | Initiate payment for a booking. | Required       |
| `GET`  | `/api/payments/verify/`        | Verify payment (Chapa callback) | Public         |

### **Prerequisite Endpoint**

| Method | Endpoint         | Description                         | Authentication |
| :--- | :--------------- |:------------------------------------| :--- |
| `POST` | `/api/bookings/` | Creates a booking to be paid for. | Required       |

---

## ⚙️ Setup and Testing Guide

### **1. Environment Setup**

**Important: Chapa API Key**

Create a `.env` file in the project root (`alx_travel_app_0x02/.env`) and add your Chapa Test Secret Key:

```bash
# .env
CHAPA_SECRET_KEY=YOUR_CHAPA_TEST_SECRET_KEY
```

### **2. Install Dependencies**

Ensure all required packages, including `chapa-python`, are installed:

```bash
# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### **3. Run the Application**

You need to run two services in separate terminals: the Django development server and the Celery worker.

```bash
# Terminal 1: Start Django development server
python manage.py runserver
```

```bash
# Terminal 2: Start Celery worker
celery -A alx_travel_app worker -l info
```

### **4. Configure Email (Optional)**
For email confirmations to be sent, configure your email backend in `alx_travel_app/settings.py`. For development, you can use the console backend to print emails to the terminal:
```python
# alx_travel_app/settings.py
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

---

## 📸 Payment Flow Demonstration (Required)

_Please replace the placeholders below with screenshots or logs that demonstrate a successful payment initiation, verification, and the resulting status update in the `Payment` model._

**(Placeholder for Screenshot 1: Initiating Payment)**
*Description: A screenshot of an API client (e.g., Postman) showing the `checkout_url` received after a `POST` request to `/api/bookings/{id}/pay/`.*

**(Placeholder for Screenshot 2: Chapa Payment Page)**
*Description: A screenshot of the user being redirected to the Chapa checkout page.*

**(Placeholder for Screenshot 3: Successful Verification Log)**
*Description: A log from the Celery worker or Django server showing the payment was successfully verified and the confirmation email task was triggered.*

**(Placeholder for Screenshot 4: Database Record Updated)**
*Description: A screenshot of the `Payment` table in the database (e.g., in DBeaver or Django admin), showing the record with a `completed` status.*

**(Placeholder for Screenshot 5: Confirmation Email in Console)**
*Description: A screenshot of the terminal running the Django server, showing the confirmation email content printed to the console.*
