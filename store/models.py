from django.db import models
from django.conf import settings
from django.contrib import admin
from django.core.validators import MinValueValidator, RegexValidator
from uuid import uuid4
from .validators import validate_file_size

# Create your models here.

# Many-Many rel with Promotion-Product


class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()


# 1-Many rel with Collection-Product


class CategoryLevelOne(models.Model):
    CROP_NURIENTS_ORGANIC = 'crop_nutrients_organic'
    CROP_NURIENTS_INORGANIC = 'crop_nutrients_inorganic'
    CROP_PROTECTION_ORGANIC = 'crop_protection_organic'
    CROP_PROTECTION_INORGANIC = 'crop_protection_inorganic'
    FARM_MACHINARIES = 'farm_machinaries'
    IMPLEMENTS = 'implements'
    CATEGORY_CHOICES = [
        (CROP_NURIENTS_ORGANIC, 'Crop Nutrients-Organic'),
        (CROP_NURIENTS_INORGANIC, 'Crop Nutrients-Inorganic'),
        (CROP_PROTECTION_ORGANIC, 'Crop Protection-Organic'),
        (CROP_PROTECTION_INORGANIC, 'Crop Protection-Inorganic'),
        (FARM_MACHINARIES, 'Farm Machinaries'),
        (IMPLEMENTS, 'Implements'),
    ]
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=50)

    def __str__(self):
        return self.category


class Collection(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='store/icons/')
    featured_product = models.ForeignKey(
        'Product', on_delete=models.SET_NULL, null=True,  related_name='+', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField(upload_to='store/images/')
    mrp_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[
        MinValueValidator(1)])
    sales_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[
        MinValueValidator(0)])
    unit = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    available = models.BooleanField(default=True)
    brand_name = models.CharField(max_length=255)
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(
        Collection, on_delete=models.CASCADE, related_name='products')
    category_level_one = models.ForeignKey(
        CategoryLevelOne, on_delete=models.PROTECT, related_name='products')

    meta_title = models.CharField(max_length=255)
    meta_description = models.TextField()
    meta_keywords = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class ProductSpecification(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='specifications')
    key1 = models.CharField(max_length=255)
    value1 = models.CharField(max_length=255)
    key2 = models.CharField(max_length=255, null=True, blank=True)
    value2 = models.CharField(max_length=255, null=True, blank=True)
    key3 = models.CharField(max_length=255, null=True, blank=True)
    value3 = models.CharField(max_length=255, null=True, blank=True)
    key4 = models.CharField(max_length=255, null=True, blank=True)
    value4 = models.CharField(max_length=255, null=True, blank=True)
    key5 = models.CharField(max_length=255, null=True, blank=True)
    value5 = models.CharField(max_length=255, null=True, blank=True)
    key6 = models.CharField(max_length=255, null=True, blank=True)
    value6 = models.CharField(max_length=255, null=True, blank=True)
    key7 = models.CharField(max_length=255, null=True, blank=True)
    value7 = models.CharField(max_length=255, null=True, blank=True)
    key8 = models.CharField(max_length=255, null=True, blank=True)
    value8 = models.CharField(max_length=255, null=True, blank=True)
    key9 = models.CharField(max_length=255, null=True, blank=True)
    value9 = models.CharField(max_length=255, null=True, blank=True)
    key10 = models.CharField(max_length=255, null=True, blank=True)
    value10 = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.product.title} - {self.key1}"


class ProductHighlight(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='highlights')
    highlight1 = models.CharField(max_length=255)
    highlight2 = models.CharField(max_length=255)
    highlight3 = models.CharField(max_length=255, null=True, blank=True)
    highlight4 = models.CharField(max_length=255, null=True, blank=True)
    highlight5 = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.product.title}"


class MetaLink(models.Model):
    external_link = models.CharField(max_length=1000)


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(
        upload_to='store/images', validators=[validate_file_size])

# Customer Model


class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'N'
    MEMBERSHIP_SILVER = 'R'
    MEMBERSHIP_GOLD = 'L'
    MEMBERSHIP_CHICES = [
        (MEMBERSHIP_BRONZE, 'Normal'),
        (MEMBERSHIP_SILVER, 'Regular'),
        (MEMBERSHIP_GOLD, 'Loyal'),
    ]

    phone = models.CharField(max_length=255)

    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHICES, default=MEMBERSHIP_BRONZE)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name}{self.user.last_name}'

    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name

    class Meta:
        ordering = ['user__first_name', 'user__last_name']
        permissions = [
            ('view_history', 'Can view history')
        ]

# Order Model


# class Order(models.Model):
#     PAYMENT_STATUS_PENDING = 'P'
#     PAYMENT_STATUS_COMPLETE = 'C'
#     PAYMENT_STATUS_FAILED = 'F'
#     PAYMENT_STATUS_CHOICES = [
#         (PAYMENT_STATUS_PENDING, 'Pending'),
#         (PAYMENT_STATUS_COMPLETE, 'Complete'),
#         (PAYMENT_STATUS_FAILED, 'Failed'),

#     ]
#     placed_at = models.DateTimeField(auto_now_add=True)
#     payment_status = models.CharField(
#         max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
#     customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

#     def __str__(self):
#         return f'Order {self.id} placed by {self.customer}'

#     class Meta:
#         permissions = [
#             ('cancel_order', 'Can cancel order')
        # ]
# 1-many rel with Order-Item


# class OrderItem(models.Model):
#     order = models.ForeignKey(
#         Order, on_delete=models.PROTECT, related_name='items')
#     product = models.ForeignKey(
#         Product, on_delete=models.PROTECT, related_name='orderitems')
#     quantity = models.PositiveSmallIntegerField()
#     unit_price = models.DecimalField(max_digits=6, decimal_places=2)


# 1-Many relationship with Customer & Address


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    Customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE)


# Shopping Cart


# class Cart(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid4)
#     created_at = models.DateTimeField(auto_now_add=True)


# 1-many rel with CartItem
# class CartItem(models.Model):
#     cart = models.ForeignKey(
#         Cart, on_delete=models.CASCADE, related_name='items')
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveSmallIntegerField(
#         validators=[MinValueValidator(1)]
#     )

#     class Meta:
#         unique_together = [['cart', 'product']]


class Review(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.IntegerField(default=0)  # Add the rating field
    date = models.DateField(auto_now_add=True)


# class Subscriber(models.Model):
#     product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
#     email = models.EmailField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ('-created_at',)

#     def __str__(self) -> str:
#         return self.email


class Shipping(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    phone = models.DecimalField(max_digits=10, decimal_places=0)
    pincode = models.DecimalField(max_digits=6, decimal_places=0)


class Banner(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='store/banner', validators=[validate_file_size]
    )

    def __str__(self) -> str:
        return self.name


class Sample(models.Model):
    name = models.CharField(max_length=255)
