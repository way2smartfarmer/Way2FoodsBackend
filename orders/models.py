from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='items')
    product_id = models.PositiveIntegerField()
    product_title = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product_title


class MyImage(models.Model):
    image = models.ImageField(upload_to='order/')

    def __str__(self):
        return self.image.name


class Contact(models.Model):
    name = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    phone = models.DecimalField(max_digits=10, decimal_places=0)
    pincode = models.DecimalField(max_digits=6, decimal_places=0)
    message = models.CharField(max_length=255)
