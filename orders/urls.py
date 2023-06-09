from django.urls import path
from .views import OrderListCreateView, MyImageView, ContactViewSet

urlpatterns = [
    path('', OrderListCreateView.as_view(), name='orders'),
    path('images', MyImageView.as_view()),
    path('contacts', ContactViewSet.as_view(
        {'get': 'list', 'post': 'create'})),
]
