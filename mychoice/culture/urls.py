"""culture app URL Configuration."""


# Django imports
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView


# Import from my app
from . import views



urlpatterns = [
    path('', TemplateView.as_view(template_name='culture/index.html'), name='index'),
    path('home/', TemplateView.as_view(template_name='culture/index.html'), name='index'),
    path('index/', TemplateView.as_view(template_name='culture/index.html'), name='index'),
    path('account/', TemplateView.as_view(template_name='culture/account.html'), name='account'),
    path('signout/', LogoutView.as_view(template_name='culture/index.html'), name='signout'),
    path('posts/', TemplateView.as_view(template_name='culture/posts.html'), name='posts'),

    # path('account/', views.account, name='account'),
    # path('account/register/', views.register, name='register'),
    # path('account/signin/', LoginView.as_view(template_name='food/signin.html'), name='signin'),
    # path('account/signout/', LogoutView.as_view(template_name='food/home.html'), name='signout'),
    # path('foodresult/', views.foodresult, name='foodresult'),
    # path('foodinfo/<int:pk>/', views.FoodInfo.as_view(), name='foodinfo'),
    # path('selection/', views.selection, name='selection'),
    # path('imprint/', TemplateView.as_view(template_name='food/imprint.html'), name='imprint'),
]