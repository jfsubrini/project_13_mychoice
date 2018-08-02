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
    path('register/', TemplateView.as_view(template_name='culture/register.html'), name='register'),
    path('signout/', LogoutView.as_view(template_name='culture/index.html'), name='signout'),
    path('contribute/', TemplateView.as_view(template_name='culture/contribute.html'), name='contribute'),
    path('features/', TemplateView.as_view(template_name='culture/features.html'), name='features'),
    path('mylist/', TemplateView.as_view(template_name='culture/mylist.html'), name='mylist'),
    path('signin/', LoginView.as_view(template_name='culture/signin.html'), name='signin'),
    path('categories/', TemplateView.as_view(template_name='culture/categories.html'), name='categories'),
    path('productinfo/', TemplateView.as_view(template_name='culture/productinfo.html'), name='productinfo'),
    # path('productinfo/<int:pk>/', views.ProductInfo.as_view(), name='productinfo'),

    # path('account/', views.account, name='account'),
    # path('account/register/', views.register, name='register'),
    # path('account/signin/', LoginView.as_view(template_name='food/signin.html'), name='signin'),
    # path('account/signout/', LogoutView.as_view(template_name='food/home.html'), name='signout'),
    # path('foodresult/', views.foodresult, name='foodresult'),
    # path('foodinfo/<int:pk>/', views.FoodInfo.as_view(), name='foodinfo'),
    # path('selection/', views.selection, name='selection'),
    # path('imprint/', TemplateView.as_view(template_name='food/imprint.html'), name='imprint'),
]