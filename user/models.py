from django.contrib.auth.models import BaseUserManager, PermissionsMixin
from django.db import models

class User(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class UserManager(PermissionsMixin, models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=30, blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    acct_type = models.CharField(max_length=30, blank=True)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'password']

    objects = BaseUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return self.first_name


class PaymentDetails(models.Model):
    token = models.CharField(max_length=70, blank=True)
    user = models.ForeignKey(UserManager, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

class Events(models.Model):
    description = models.CharField(max_length=250, blank=True)
    location = models.CharField(max_length=50, blank=True)
    location_tip = models.CharField(max_length=250, blank=True)
    event_type = models.CharField(max_length=250, blank=True)
    virtual_meet_link = models.URLField()
    category = models.CharField(max_length=50, blank=True)
    custom_url = models.URLField()
    frequency = models.IntegerField()
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    twitter_url = models.URLField()
    facebook_url = models.URLField()
    instagram_url = models.URLField()
    user = models.ForeignKey(UserManager, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

class Tickets(models.Model):
    name = models.CharField(max_length=30, blank=True)
    description = models.CharField(max_length=250, blank=True)
    ticket_type = models.CharField(max_length=50, blank=True)
    stock = models.CharField(max_length=250, blank=False)
    no_of_stock = models.IntegerField()
    purchase_limit = models.IntegerField()
    price = models.IntegerField()
    event = models.ForeignKey(UserManager, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

class TicketTransactions(models.Model):
    user = models.ForeignKey(UserManager, on_delete=models.CASCADE)
    ticket = models.ForeignKey(UserManager, on_delete=models.CASCADE)
    fee = models.IntegerField()
    status_choices = ( ('Successful', 'Successful'),
        ('Pending', 'Pending'),
        ('Failed', 'Failed'),
    )
    status = models.CharField(max_length=20, choices=status_choices, default="status")
    no_of_purchase = models.IntegerField()
    amount = models.IntegerField()
    transaction_ticket_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f'{self.user.email} - {self.ticket.name}'

    def get_total_amount(self):
        return self.amount + self.fee