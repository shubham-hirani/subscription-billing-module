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
