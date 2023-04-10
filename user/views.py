from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.db.models.query import QuerySet
from rest_framework.generics import RetrieveAPIView, ListAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, PaymentDetailsSerializer, EventsSerializer, TicketsSerializer, TicketTransactionsSerializer
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

    
class PaymentDetailsView(GenericAPIView):
    queryset = PaymentDetails.objects.all()
    serializer = PaymentDetailsSerializer(PaymentDetails, many=True)
    
    def list(self,request):
          queryset  = self.PaymentDetails.objects.all() 
          serializer = PaymentDetailsSerializer(self.get_queryset(), many=True)
          return response.Response(serializer.data)

class EventsView(GenericAPIView):
    queryset = Events.objects.all()
    serializer = EventsSerializer(Events, many=True)
    
    def list(self,request):
          queryset  = self.Events.objects.all() 
          serializer = EventsSerializer(self.get_queryset(), many=True)
          return response.Response(serializer.data)

class TicketView(GenericAPIView):
    queryset = Tickets.objects.all()
    serializer = TicketsSerializer(Tickets, many=True)

    def list(self,request):
          queryset  = self.Tickets.objects.all() 
          serializer = TicketsSerializer(self.get_queryset(), many=True)
          return response.Response(serializer.data)


class TicketTransactionsView(GenericAPIView):
    queryset = TicketTransactions.objects.all()
    serializer = TicketTransactionsSerializer

    def list(self,request):
          queryset  = self.TicketTransactions.objects.all() 
          serializer = TicketTransactionsSerializer(self.get_queryset(), many=True)
          return response.Response(serializer.data)