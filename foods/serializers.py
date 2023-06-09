from rest_framework import serializers
from .models import Category, MajorVegetables, MetaLink, Shipping, Banner, RegularVegetables, OtherVegetables, LeafyVegetables, ExoticVegetables, MajorFruits, ExoticFruits, Grains, Spices, Oils, SpecialPackages


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'title', 'image', 'description', 'slug',
                  'meta_title', 'meta_description', 'meta_keywords']


class MajorVegetablesSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = MajorVegetables
        fields = ['id', 'title', 'image', 'slug', 'price', 'unit',
                  'available', 'meta_title', 'meta_description', 'meta_keywords']


class RegularVegetablesSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = RegularVegetables
        fields = ['id', 'title', 'image', 'slug', 'price', 'unit',
                  'available', 'meta_title', 'meta_description', 'meta_keywords']


class OtherVegetablesSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = OtherVegetables
        fields = ['id', 'title', 'image', 'slug', 'price', 'unit',
                  'available', 'meta_title', 'meta_description', 'meta_keywords']


class LeafyVegetablesSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = LeafyVegetables
        fields = ['id', 'title', 'image', 'slug', 'price', 'unit',
                  'available', 'meta_title', 'meta_description', 'meta_keywords']


class ExoticVegetablesSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = ExoticVegetables
        fields = ['id', 'title', 'image', 'slug', 'price', 'unit',
                  'available', 'meta_title', 'meta_description', 'meta_keywords']


class MajorFruitsSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = MajorFruits
        fields = ['id', 'title', 'image', 'slug', 'price', 'unit',
                  'available', 'meta_title', 'meta_description', 'meta_keywords']


class ExoticFruitsSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = ExoticFruits
        fields = ['id', 'title', 'image', 'slug', 'price', 'unit',
                  'available', 'meta_title', 'meta_description', 'meta_keywords']


class GrainsSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Grains
        fields = ['id', 'title', 'image', 'slug', 'price', 'unit',
                  'available', 'meta_title', 'meta_description', 'meta_keywords']


class SpicesSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Spices
        fields = ['id', 'title', 'image', 'slug', 'price', 'unit',
                  'available', 'meta_title', 'meta_description', 'meta_keywords']


class OilsSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Oils
        fields = ['id', 'title', 'image', 'slug', 'price', 'unit',
                  'available', 'meta_title', 'meta_description', 'meta_keywords']


class SpecialPackagesSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = SpecialPackages
        fields = ['id', 'title', 'image', 'slug', 'price', 'unit', 'description',
                  'available', 'meta_title', 'meta_description', 'meta_keywords']


class ShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipping
        fields = '__all__'


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class MetaLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaLink
        fields = '__all__'
