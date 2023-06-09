from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator
from .validators import validate_file_size
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='store/images/')
    description = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    meta_title = models.CharField(max_length=255, default='None')
    meta_description = models.TextField(default='None')
    meta_keywords = models.TextField(default="None")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class MajorVegetables(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='store/images/')
    slug = models.SlugField(max_length=255, unique=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    unit = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    meta_title = models.CharField(max_length=255, default='None')
    meta_description = models.TextField(default='None')
    meta_keywords = models.TextField(default="None")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class RegularVegetables(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='store/images/')
    slug = models.SlugField(max_length=255, unique=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    unit = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    meta_title = models.CharField(max_length=255, default='None')
    meta_description = models.TextField(default='None')
    meta_keywords = models.TextField(default="None")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class OtherVegetables(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='store/images/')
    slug = models.SlugField(max_length=255, unique=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    unit = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    meta_title = models.CharField(max_length=255)
    meta_description = models.TextField()
    meta_keywords = models.TextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class LeafyVegetables(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='store/images/')
    slug = models.SlugField(max_length=255, unique=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    unit = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    meta_title = models.CharField(max_length=255)
    meta_description = models.TextField()
    meta_keywords = models.TextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class ExoticVegetables(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='store/images/')
    slug = models.SlugField(max_length=255, unique=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    unit = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    meta_title = models.CharField(max_length=255)
    meta_description = models.TextField()
    meta_keywords = models.TextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class MajorFruits(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='store/images/')
    slug = models.SlugField(max_length=255, unique=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    unit = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    meta_title = models.CharField(max_length=255)
    meta_description = models.TextField()
    meta_keywords = models.TextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class ExoticFruits(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='store/images/')
    slug = models.SlugField(max_length=255, unique=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    unit = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    meta_title = models.CharField(max_length=255)
    meta_description = models.TextField()
    meta_keywords = models.TextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Grains(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='store/images/')
    slug = models.SlugField(max_length=255, unique=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    unit = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    meta_title = models.CharField(max_length=255)
    meta_description = models.TextField()
    meta_keywords = models.TextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Spices(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='store/images/')
    slug = models.SlugField(max_length=255, unique=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    unit = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    meta_title = models.CharField(max_length=255)
    meta_description = models.TextField()
    meta_keywords = models.TextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Oils(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='store/images/')
    slug = models.SlugField(max_length=255, unique=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    unit = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    meta_title = models.CharField(max_length=255)
    meta_description = models.TextField()
    meta_keywords = models.TextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class SpecialPackages(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='store/images/')
    slug = models.SlugField(max_length=255, unique=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    unit = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    description = models.TextField()
    meta_title = models.CharField(max_length=255)
    meta_description = models.TextField()
    meta_keywords = models.TextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class MetaLink(models.Model):
    external_link = models.CharField(max_length=1000)


class Banner(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='banner', validators=[validate_file_size]
    )

    def __str__(self) -> str:
        return self.name


class Shipping(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    phone = models.DecimalField(max_digits=10, decimal_places=0)
    pincode = models.DecimalField(max_digits=6, decimal_places=0)
