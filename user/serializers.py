from rest_framework import serializers
from .models import User, PaymentDetails, Events, Tickets, TicketTransactions


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'password', 'country', 'acct_type')

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class PaymentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetails
        fields = ('token', 'user', 'created_at', 'updated_at')


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ('description', 'location', 'location_tip', 'event_type', 'virtual_meet_link', 'category', 'custon_url','frequency', 'start_date', 'start_time', 'end_date', 'end_time', 'twitter_url', 'facebook_url', 'instagram_url', 'user', 'created_at', 'updated_at')


class TicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = ('name', 'description', 'ticket_type', 'stock', 'no_of_stock', 'purchase_limit', 'price', 'event', 'created_at', 'updated_at')


class TicketTransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketTransactions
        fields = ('user', 'ticket', 'fee', 'status', 'no_of_purchase', 'amount', 'ticket_id', 'created_at', 'updated_at')
        