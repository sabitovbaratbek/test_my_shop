from django.contrib import admin
from .models import *
from products.models import Product

class ProductInline(admin.StackedInline):
    model = Product
    extra = 0
class ProductInOrderInline(admin.StackedInline):
    model = ProductInOrder
    extra = 0
class ProductInBasketInline(admin.StackedInline):
    model = ProductInBasket
    extra = 0

class OrderInline(admin.StackedInline):
    model = Order
    extra = 0

class StatusAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]
    inlines = [OrderInline]
    class Meta:
        model = Status

admin.site.register(Status, StatusAdmin)


class OrderAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    inlines = [ProductInOrderInline,ProductInBasketInline]
    

    class Meta:
        model = Order

admin.site.register(Order, OrderAdmin)


class ProductInOrderAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductInOrder._meta.fields]
    
    class Meta:
        model = ProductInOrder

admin.site.register(ProductInOrder, ProductInOrderAdmin)


class ProductInBasketAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductInBasket._meta.fields]
   
    class Meta:
        model = ProductInBasket

admin.site.register(ProductInBasket, ProductInBasketAdmin)
