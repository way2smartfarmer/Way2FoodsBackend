from rest_framework.generics import ListCreateAPIView
from .serializers import CategorySerializer, MetaLinkSerializer, MajorVegetablesSerializer, RegularVegetablesSerializer, OtherVegetablesSerializer, LeafyVegetablesSerializer, ExoticVegetablesSerializer, MajorFruitsSerializer, ExoticFruitsSerializer, GrainsSerializer, SpicesSerializer, OilsSerializer, SpecialPackagesSerializer, BannerSerializer, ShippingSerializer
from .models import Category, MajorVegetables, RegularVegetables, OtherVegetables, LeafyVegetables, ExoticVegetables, MajorFruits, ExoticFruits, Grains, Spices, Oils, SpecialPackages, Shipping, MetaLink, Banner
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet


class category(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class major_vegetables(ListCreateAPIView):
    queryset = MajorVegetables.objects.all()
    serializer_class = MajorVegetablesSerializer
    lookup_field = 'slug'


class regular_vegetables(ListCreateAPIView):
    queryset = RegularVegetables.objects.all()
    serializer_class = RegularVegetablesSerializer
    lookup_field = 'slug'


class other_vegetables(ListCreateAPIView):
    queryset = OtherVegetables.objects.all()
    serializer_class = OtherVegetablesSerializer
    lookup_field = 'slug'


class leafy_vegetables(ListCreateAPIView):
    queryset = LeafyVegetables.objects.all()
    serializer_class = LeafyVegetablesSerializer
    lookup_field = 'slug'


class exotic_vegetables(ListCreateAPIView):
    queryset = ExoticVegetables.objects.all()
    serializer_class = ExoticVegetablesSerializer
    lookup_field = 'slug'


class major_fruits(ListCreateAPIView):
    queryset = MajorFruits.objects.all()
    serializer_class = MajorFruitsSerializer
    lookup_field = 'slug'


class exotic_fruits(ListCreateAPIView):
    queryset = ExoticFruits.objects.all()
    serializer_class = ExoticFruitsSerializer
    lookup_field = 'slug'


class grains(ListCreateAPIView):
    queryset = Grains.objects.all()
    serializer_class = GrainsSerializer
    lookup_field = 'slug'


class spices(ListCreateAPIView):
    queryset = Spices.objects.all()
    serializer_class = SpicesSerializer
    lookup_field = 'slug'


class oils(ListCreateAPIView):
    queryset = Oils.objects.all()
    serializer_class = OilsSerializer
    lookup_field = 'slug'


class special_packages(ListCreateAPIView):
    queryset = SpecialPackages.objects.all()
    serializer_class = SpecialPackagesSerializer
    lookup_field = 'slug'


class ShippingViewSet(ModelViewSet):
    queryset = Shipping.objects.all()
    serializer_class = ShippingSerializer


class BannerViewSet(ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer


class MetaLinkViewSet(ModelViewSet):
    queryset = MetaLink.objects.all()
    serializer_class = MetaLinkSerializer
