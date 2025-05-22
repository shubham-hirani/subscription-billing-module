from celery import shared_task
from django.utils import timezone

from .models import Subscription, Invoice


@shared_task
def generate_invoices():
    today = timezone.now().date()
    subscriptions = Subscription.objects.filter(start_date__day=today.day, status='active')
    for sub in subscriptions:
        Invoice.objects.create(user=sub.user, plan=sub.plan, amount=sub.plan.price, issue_date=today,
            due_date=today + timezone.timedelta(days=7))


@shared_task
def mark_overdue_invoices():
    today = timezone.now().date()
    Invoice.objects.filter(due_date__lt=today, status='pending').update(status='overdue')


@shared_task
def send_invoice_reminders():
    pending_invoices = Invoice.objects.filter(status='pending')
    for invoice in pending_invoices:
        print(f'Reminder: Invoice #{invoice.id} for {invoice.user.username} is still unpaid.')

# from celery import shared_task
#
# @shared_task
# def test_task():
#     print("Test task executed successfully.")
#     return "done"
