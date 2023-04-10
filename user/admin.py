from django.contrib import admin
from .models import UserManager, PaymentDetails, Events, Tickets, TicketTransactions


myModels = [UserManager, PaymentDetails, Events, Tickets, TicketTransactions]
admin.site.register(myModels)