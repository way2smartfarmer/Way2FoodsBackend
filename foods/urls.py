from django.urls import path
from .views import category, major_vegetables, regular_vegetables, other_vegetables, leafy_vegetables, exotic_vegetables, major_fruits, exotic_fruits, grains, spices, oils, special_packages, BannerViewSet, ShippingViewSet, MetaLinkViewSet
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('shop/', category.as_view(), name='category-detail'),
    path('essential-and-regular-vegetables/',
         regular_vegetables.as_view(), name='regular_vegetables'),
    path('major-vegetables/', major_vegetables.as_view(), name='major_vegetables'),
    path('other-vegetables/', other_vegetables.as_view(), name='other_vegetables'),
    path('leafy-vegetables/', leafy_vegetables.as_view(), name='leafy_vegetables'),
    path('exotic-vegetables/', exotic_vegetables.as_view(),
         name='exotic_vegetables'),
    path('major-seasonal-and-other-fruits/',
         major_fruits.as_view(), name='major_fruits'),
    path('exotic-and-imported-fruits/',
         exotic_fruits.as_view(), name='exotic_fruits'),
    path('grains-pulses-and-millets/', grains.as_view(), name='grains'),
    path('spices-plantation-and-nuts/', spices.as_view(), name='spices'),
    path('oils-seeds-and-others/', oils.as_view(), name='oils'),
    path('special-packages/', special_packages.as_view(), name='special_packages'),
    path('banner/',
         BannerViewSet.as_view({'get': 'list', 'post': 'create'}), name='banner'),
    path('links/',
         MetaLinkViewSet.as_view({'get': 'list', 'post': 'create'}), name='link'),
    path('shipping/',
         ShippingViewSet.as_view({'get': 'list', 'post': 'create'}), name='shipping'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
