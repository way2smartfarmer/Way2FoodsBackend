# Generated by Django 4.2 on 2023-06-09 09:59

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import store.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='store/banner', validators=[store.validators.validate_file_size])),
            ],
        ),
        migrations.CreateModel(
            name='CategoryLevelOne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('crop_nutrients_organic', 'Crop Nutrients-Organic'), ('crop_nutrients_inorganic', 'Crop Nutrients-Inorganic'), ('crop_protection_organic', 'Crop Protection-Organic'), ('crop_protection_inorganic', 'Crop Protection-Inorganic'), ('farm_machinaries', 'Farm Machinaries'), ('implements', 'Implements')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='store/icons/')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='MetaLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_link', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='store/images/')),
                ('mrp_price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(1)])),
                ('sales_price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('unit', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(default=0)),
                ('available', models.BooleanField(default=True)),
                ('brand_name', models.CharField(max_length=255)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('meta_title', models.CharField(max_length=255)),
                ('meta_description', models.TextField()),
                ('meta_keywords', models.TextField()),
                ('category_level_one', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='store.categorylevelone')),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='store.collection')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('discount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('phone', models.DecimalField(decimal_places=0, max_digits=10)),
                ('pincode', models.DecimalField(decimal_places=0, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('rating', models.IntegerField(default=0)),
                ('date', models.DateField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='store.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductSpecification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key1', models.CharField(max_length=255)),
                ('value1', models.CharField(max_length=255)),
                ('key2', models.CharField(blank=True, max_length=255, null=True)),
                ('value2', models.CharField(blank=True, max_length=255, null=True)),
                ('key3', models.CharField(blank=True, max_length=255, null=True)),
                ('value3', models.CharField(blank=True, max_length=255, null=True)),
                ('key4', models.CharField(blank=True, max_length=255, null=True)),
                ('value4', models.CharField(blank=True, max_length=255, null=True)),
                ('key5', models.CharField(blank=True, max_length=255, null=True)),
                ('value5', models.CharField(blank=True, max_length=255, null=True)),
                ('key6', models.CharField(blank=True, max_length=255, null=True)),
                ('value6', models.CharField(blank=True, max_length=255, null=True)),
                ('key7', models.CharField(blank=True, max_length=255, null=True)),
                ('value7', models.CharField(blank=True, max_length=255, null=True)),
                ('key8', models.CharField(blank=True, max_length=255, null=True)),
                ('value8', models.CharField(blank=True, max_length=255, null=True)),
                ('key9', models.CharField(blank=True, max_length=255, null=True)),
                ('value9', models.CharField(blank=True, max_length=255, null=True)),
                ('key10', models.CharField(blank=True, max_length=255, null=True)),
                ('value10', models.CharField(blank=True, max_length=255, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specifications', to='store.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='store/images', validators=[store.validators.validate_file_size])),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='store.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductHighlight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highlight1', models.CharField(max_length=255)),
                ('highlight2', models.CharField(max_length=255)),
                ('highlight3', models.CharField(blank=True, max_length=255, null=True)),
                ('highlight4', models.CharField(blank=True, max_length=255, null=True)),
                ('highlight5', models.CharField(blank=True, max_length=255, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='highlights', to='store.product')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=255)),
                ('membership', models.CharField(choices=[('N', 'Normal'), ('R', 'Regular'), ('L', 'Loyal')], default='N', max_length=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user__first_name', 'user__last_name'],
                'permissions': [('view_history', 'Can view history')],
            },
        ),
        migrations.AddField(
            model_name='collection',
            name='featured_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='store.product'),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.customer')),
            ],
        ),
    ]
