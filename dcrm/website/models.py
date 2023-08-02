from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=80)
    contact_details = models.TextField()
    additional_info = models.TextField(blank=True)  # Optional field, can be blank
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=80)
    contact_details = models.TextField()
    additional_info = models.TextField(blank=True)  # Optional field, can be blank
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    order_number = models.CharField(max_length=50, unique=True)
    order_type = models.CharField(max_length=50)
    order_details = models.TextField()
    term = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    order_price = models.DecimalField(max_digits=7, decimal_places=2)
    author_price = models.DecimalField(max_digits=7, decimal_places=2)
    additional_info = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.order_number
