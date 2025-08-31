from django.db import models

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, verbose_name='Название')

    def __str__(self):
        return self.name
    

class User(models.Model):
    user_id = models.BigIntegerField(primary_key=True, unique=True, verbose_name="Telegram ID")
    email = models.TextField(max_length=255, verbose_name="Email", unique=True, blank=True, null=True)
    phone = models.BigIntegerField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.email if self.email else f"User {self.user_id}"


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    photo = models.ImageField(upload_to='product_photos/', blank=True, null=True, verbose_name="Фото")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Категория")

    def __str__(self):
        return self.name



class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    quantity = models.IntegerField(default=1, verbose_name='Количество')

    def __str__(self):
        return f"Корзина {self.user.user_id} - {self.product.name} x {self.quantity}"