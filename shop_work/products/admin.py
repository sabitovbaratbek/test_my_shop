from django.contrib import admin
from .models import *
from orders.models import ProductInBasket


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 0
class ProductInBasketInline(admin.StackedInline):
    model = ProductInBasket
    extra = 0

class ProductInline(admin.StackedInline):
    model = Product
    extra = 0
  
# class ProductInBasketInline(admin.StackedInline):
#     model = ProductInBasket
#     fields = ("name","price","discount", "category", "short_description ", "description", "is_active", "created", "updated")  

# class ProductInBasketAdmin(admin.ModelAdmin):
#     fields = ("name","price","discount", "category", "short_description ", "description", "is_active", "created", "updated") 
#     # inlines = [ProductInBasketInline]
    
    # class Meta:
    #     model = ProductInBasket

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductCategory._meta.fields]
    inlines = [ProductInline]
    class Meta:
        model = ProductCategory

admin.site.register(ProductCategory, ProductCategoryAdmin)


class ProductAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImageInline,ProductInBasketInline]
   
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)


class ProductImageAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]

    class Meta:
        model = ProductImage

admin.site.register(ProductImage, ProductImageAdmin)