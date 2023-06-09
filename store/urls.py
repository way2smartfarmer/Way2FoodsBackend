from django.urls import path, include
from rest_framework_nested import routers

from . import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet, basename='products')
router.register(r'collections', views.CollectionViewSet)
# router.register(r'carts', views.CartViewSet)
# router.register(r'customers', views.CustomerViewSet)
# router.register(r'orders', views.OrderViewSet, basename='orders')
router.register(r'shipping', views.ShippingViewSet, basename='shippings')
router.register(r'banners', views.BannerViewSet, basename='banners')
router.register(r'links', views.MetaLinkViewSet, basename='links')

products_router = routers.NestedSimpleRouter(
    router, r'products',lookup='product')
# products_router.register(
#     r'subscribe', views.SubscribeToProduct, basename='product-subscribe')
# products_router.register(r'reviews', views.ReviewViewSet,
#                          basename='product-reviews')

# carts_router = routers.NestedSimpleRouter(router, r'carts', lookup='cart')
# carts_router.register(r'items', views.CartItemViewSet, basename='cart-items')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(products_router.urls)),
    # path('', include(carts_router.urls)),
    path('api/search/', views.search_products, name='search_products'),
    #     path('subscribe', views.SubscribeToProduct.as_view(), name='subscribe'),
    path('products/<slug:slug>/', views.ProductViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='product-detail'),
    path('products/',
         views.ProductViewSet.as_view({'get': 'list', 'post': 'create'})),

]
