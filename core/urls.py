from django.views.generic import TemplateView
from django.urls import path
from . import views

# URL config
urlpatterns = [
    path('', TemplateView.as_view(template_name='core/index.html')),
    path("auth/users/reset_password/", views.forgot_password),
    path("auth/users/reset_password_confirm/", views.reset_password),
]
