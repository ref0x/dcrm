from django.db import models


class Order(models.Model):
    """
    1. Order number
    2. type
    3. Term
    4. Customer contacts
    5. Order price
    6. Author's price
    """

    additional_info = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Customer(models.Model):
    name = models.CharField(max_length=80)
    contact_details = models.TextField()
    additional_info = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Author(models.Model):
    name = models.CharField(max_length=80)
    contact_details = models.TextField()
    additional_info = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
