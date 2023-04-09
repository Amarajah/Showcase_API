from django.contrib.auth import get_user_model
from django.http import JsonResponse
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializer import UserSerializer, PaymentDetailsSerializer, EventsSerializer, TicketsSerializer, TicketTransactionsSerializer
from .models import User, PaymentDetails, Events, Tickets, TicketTransactions


class UserAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return response.Response(serializer.data)

    
def payment_details(request):
    payments = PaymentDetails.objects.all()
    serializer = PaymentDetailsSerializer(PaymentDetails, many=True)
    return JsonResponse(serializer.data)


def events(request):
    events = Events.objects.all()
    serializer = EventsSerializer(Events, many=True)
    return JsonResponse(serializer.data)


def ticketing(request):
    tickets = Tickets.objects.all()
    serializer = TicketsSerializer(Tickets, many=True)
    return JsonResponse(serializer.data)


class ticket_transactions(request):
    transactions = TicketTransactions.objects.all()
    serializer = TicketTransactionsSerializer(TicketTransactions, many=True)
    return JsonResponse(serializer.data)