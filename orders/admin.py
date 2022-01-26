from django.contrib import admin
from .models import *


class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0


class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'product', 'nmb', 'price_per_item', 'total_price', 'is_active', 'created', 'updated']

    class Meta:
        model = ProductInOrder


admin.site.register(ProductInOrder, ProductInOrderAdmin)


class StatusAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'created', 'updated']

    class Meta:
        model = Status


admin.site.register(Status, StatusAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_name', 'customer_email', 'customer_phone', 'customer_address', 'comments',
                    'status', 'total_price', 'created', 'updated']
    inlines = [ProductInOrderInline]

    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)


class ProductInBasketAdmin(admin.ModelAdmin):
    list_display = ['session_key','id', 'order', 'product', 'nmb', 'price_per_item', 'total_price', 'is_active', 'created', 'updated']

    class Meta:
        model = ProductInBasket


admin.site.register(ProductInBasket, ProductInBasketAdmin)
