from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Plan, Subscription, Invoice
from datetime import timedelta

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def subscribe(request):
    plan_id = request.data.get("plan_id")
    if not plan_id:
        return Response({"error": "plan_id is required"}, status=400)

    plan = get_object_or_404(Plan, id=plan_id)
    user = request.user

    subscription, created = Subscription.objects.update_or_create(
        user=user,
        defaults={
            "plan": plan,
            "start_date": timezone.now().date(),
            "end_date": timezone.now().date() + timedelta(days=7),
            "status": "active",
        }
    )
    return Response({"message": "Subscribed successfully", "subscription_id": subscription.id})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unsubscribe(request):
    user = request.user
    try:
        subscription = Subscription.objects.get(user=user, status="active")
    except Subscription.DoesNotExist:
        return Response({"error": "Active subscription not found"}, status=404)

    subscription.status = "cancelled"
    subscription.end_date = timezone.now().date()
    subscription.save()

    return Response({"message": "Unsubscribed successfully"})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def pay_invoice(request):
    user = request.user
    invoice_id = request.data.get('invoice_id')
    if not invoice_id:
        return Response({"error": "invoice_id is required"}, status=400)
    try:
        invoice_details = Invoice.objects.get(user=user, status="pending", id=invoice_id)
    except Invoice.DoesNotExist:
        return Response({"error": "No pending invoice found not found"}, status=404)
    invoice_details.status = "paid"
    invoice_details.save()

    return Response({"message": "Invoice paid successfully"})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def invoice_list(request):
    user = request.user
    invoices = Invoice.objects.filter(user=user).order_by('-issue_date')

    data = []
    for invoice in invoices:
        data.append({
            "id": invoice.id,
            "plan": invoice.plan.name,
            "amount": invoice.amount,
            "issue_date": invoice.issue_date,
            "due_date": invoice.due_date,
            "status": invoice.status,
        })

    return Response(data)


