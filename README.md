# 💳 Django Subscription Billing Module

This is a Django-based web application that supports user sign-up, login via JWT, and periodic invoice generation using Celery. It’s designed as a modular subscription billing system.

---

## 🚀 Features

- 🔐 JWT-based Authentication (using Django REST Framework)
- 📅 Periodic Invoice Generation (using Celery + Redis)
- 🧾 Subscription Plans and Billing Cycles
- 🛠️ Admin Management Portal
- 📦 API-ready for integration with external systems

---

## 🧰 Tech Stack

- **Backend:** Django, Django REST Framework
- **Async Tasks:** Celery with Redis
- **Auth:** JWT (via `djangorestframework-simplejwt`)
- **Database:** SQLite (default) – can be swapped for PostgreSQL
- **Task Scheduling:** Celery Beat
- **Deployment-ready:** Docker (optional)

---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/your-username/subscription-billing-module.git
cd subscription-billing-module

# Create a virtual environment
python -m venv .venv
source .venv/Scripts/activate  # On Windows
# Or
source .venv/bin/activate      # On macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start the development server
python manage.py runserver


Make sure Redis is running
#Running Celery and Redis in local
docker run -p 6379:6379 redis

#Start celery server
celery -A subscription_billing_module worker --loglevel=info

#To run periodic task with celery beat
celery -A subscription_billing_module beat --loglevel=info
```

#cURL examples

Signup example cURL
```bash
curl --location 'http://localhost:8000/api/auth/signup/' \
--header 'Content-Type: application/json' \
--data '{"username":"testuser", "password":"password123"}'
```

Login example cURL
```bash
curl --location 'http://localhost:8000/api/auth/login/' \
--header 'Content-Type: application/json' \
--data '{
    "username": "testuser",
    "password": "password123"
}'
```

Subscribe plan example cURL
```bash
curl --location 'http://localhost:8000/api/subscribe/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ3OTM4OTQ3LCJpYXQiOjE3NDc5Mzg2NDcsImp0aSI6ImE3MGMzZjdiYjM2MTRjMWU4ODc1OTk3YTc5ZjgxNDkwIiwidXNlcl9pZCI6Mn0.kpLJm4ylTF9Cph8ShQ9WPoCbHf31IWikSa6W3T_T8dg' \
--header 'Content-Type: application/json' \
--data '{
    "plan_id": 1
}'
```

unsubscribe example cURL
```bash
curl --location 'http://localhost:8000/api/unsubscribe/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ3OTMyMTAzLCJpYXQiOjE3NDc5MzE4MDMsImp0aSI6IjRiMGEyZmNiY2YxZDRlZDBhMjBmMDZiYTBjODZkN2I1IiwidXNlcl9pZCI6Mn0.I7-s3GzdiLP9fVVZQPeLmbJTQP48JHzbFv_Gaf8P1pY' \
--header 'Content-Type: application/json' \
--data '{
    "plan_id": 1
}'
```


Invoice payment example cURL
```bash
curl --location 'http://localhost:8000/api/pay_invoice/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ3OTM4OTQ3LCJpYXQiOjE3NDc5Mzg2NDcsImp0aSI6ImE3MGMzZjdiYjM2MTRjMWU4ODc1OTk3YTc5ZjgxNDkwIiwidXNlcl9pZCI6Mn0.kpLJm4ylTF9Cph8ShQ9WPoCbHf31IWikSa6W3T_T8dg' \
--header 'Content-Type: application/json' \
--data '{
    "invoice_id": 1
}'
```

Invoice list example cURL
```bash
curl --location --request GET 'http://localhost:8000/api/invoice_list/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ3OTM4OTQ3LCJpYXQiOjE3NDc5Mzg2NDcsImp0aSI6ImE3MGMzZjdiYjM2MTRjMWU4ODc1OTk3YTc5ZjgxNDkwIiwidXNlcl9pZCI6Mn0.kpLJm4ylTF9Cph8ShQ9WPoCbHf31IWikSa6W3T_T8dg' \
--header 'Content-Type: application/json' \
--data '{
    "invoice_id": 1
}'
```
