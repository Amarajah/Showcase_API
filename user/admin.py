from django.contrib import admin
from .models import User, PaymentDetails, Events, Tickets, TicketTransactions

admin.site.register(User)
admin.site.register(PaymentDetails)
admin.site.register(Events)
admin.site.register(Tickets)
admin.site.register(TicketTransactions)