from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.db.models.query import QuerySet
from rest_framework.generics import RetrieveAPIView, ListAPIView, GenericAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, PaymentDetailsSerializer, EventsSerializer, TicketsSerializer, TicketTransactionsSerializer
from .models import User, PaymentDetails, Events, Tickets, TicketTransactions, UserManager


class UserAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return response.Response(serializer.data)

    
class PaymentDetailsView(ListCreateAPIView):
    queryset = PaymentDetails.objects.all()
    serializer = PaymentDetailsSerializer

    def post(self, request, *args, **kwargs):
        serializer = PaymentDetailsSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        data = serializer.data
        data['user'] = UserManager.objects.get(id=data['user'])
        print(data)
        
        payment = PaymentDetails(**data)
        payment.save()

        return Response(data)

   
class EventsView(ListCreateAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer

    def post(self, request, *args, **kwargs):
        serializer = EventsSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        data = serializer.data
        data['user'] = UserManager.objects.get(id=data['user'])
        print(data)
        
        event = Events(**data)
        event.save()

        return Response(data)

class TicketView(ListCreateAPIView):
    queryset = Tickets.objects.all()
    serializer = TicketsSerializer(Tickets, many=True)

    def post(self, request, *args, **kwargs):
        serializer = TicketsSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        data = serializer.data
        data['user'] = UserManager.objects.get(id=data['user'])
        print(data)
        
        tickett = Tickets(**data)
        ticket.save()

        return Response(data)


class TicketTransactionsView(ListCreateAPIView):
    queryset = TicketTransactions.objects.all()
    serializer = TicketTransactionsSerializer

    def post(self, request, *args, **kwargs):
        serializer = TicketTransactionsSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        data = serializer.data
        data['user'] = UserManager.objects.get(id=data['user'])
        print(data)
        
        ticket_transact = TicketTransactions(**data)
        ticket_transact.save()

        return Response(data)