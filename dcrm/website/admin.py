from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Order, Customer, Author


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "order_name",
        "order_type",
        "term",
        "link_to_customer",
        "link_to_author",
        # "customer",
        # "author",
        "author_price",
        "order_price",
        "is_closed",

    )

    def link_to_customer(self, obj):
        if obj.customer is not None:
            link = reverse("admin:website_customer_change", args=[obj.customer.id])
            return format_html('<a href="{}">{}</a>', link, obj.customer.name)
        else:
            return "(no customer)"

    def link_to_author(self, obj):
        if obj.author is not None:
            link = reverse("admin:website_author_change", args=[obj.author.id])
            return format_html('<a href="{}">{}</a>', link, obj.author.name)
        else:
            return "(no author)"

    link_to_customer.short_description = "Customer"
    link_to_author.short_description = "Author"  # Название столбца


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at", "updated_at", "num_orders")

    def num_orders(self, obj):
        return Order.objects.filter(customer=obj).count()

    num_orders.short_description = "Number of Orders"


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at", "updated_at", "num_orders")

    def num_orders(self, obj):
        return Order.objects.filter(author=obj).count()

    num_orders.short_description = "Number of Orders"
