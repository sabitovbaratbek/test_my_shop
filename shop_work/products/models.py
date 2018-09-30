from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, blank=True,verbose_name = "Категория товара", null=True, default=None)
    is_active = models.BooleanField(default=True,verbose_name = "Имеется в продаже",)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категория товаров'


class Product(models.Model):
    name = models.CharField(max_length=64,verbose_name = "Товары", blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=10,verbose_name = "Цена", decimal_places=2, default=0)
    discount = models.IntegerField(default=0,verbose_name = "Скидка",)
    category = models.ForeignKey(ProductCategory,verbose_name = "Категория товара", blank=True, null=True, default=None,on_delete = models.CASCADE)
    short_description = models.TextField(blank=True,verbose_name = "Краткое описание товара", null=True, default=None)
    description = models.TextField(blank=True,verbose_name = "Полное описание товара",  null=True, default=None)
    is_active = models.BooleanField(default=True,verbose_name = "Имеется в продаже")
    created = models.DateTimeField(auto_now_add=True,verbose_name = "Дата выпуска", auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,verbose_name = "Годен до:", auto_now=True)

    def __str__(self):
        return "%s, %s" % (self.price, self.name)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None,on_delete = models.CASCADE)
    image = models.ImageField(upload_to='products_images/')
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'