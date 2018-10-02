"""culture app URL Configuration."""


# Django imports
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
    )

# Import from my app
from . import views



urlpatterns = [
    # Homepage
    path('', TemplateView.as_view(template_name='culture/index.html'), name='index'),
    path('home/', TemplateView.as_view(template_name='culture/index.html'), name='index'),
    path('index/', TemplateView.as_view(template_name='culture/index.html'), name='index'),
    #### Account
    path('account/register/', TemplateView.as_view(template_name='culture/account/register.html'), name='register'),
    path('account/signin/', LoginView.as_view(template_name='culture/account/signin.html'), name='signin'),
    path('account/signout/', LogoutView.as_view(template_name='culture/index.html'), name='signout'),
    #### Password reset
    path('account/password_reset/', PasswordResetView.as_view(
        template_name='culture/account/password_reset.html',
        email_template_name='culture/account/password_reset_email.html',
        subject_template_name='culture/account/password_reset_subject.txt'), name='password_reset'
        ),
    path('account/password_reset_done/', PasswordResetDoneView.as_view(
        template_name='culture/account/password_reset_done.html'), name='password_reset_done'
        ),
    re_path(
        r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        PasswordResetConfirmView.as_view(
            template_name='culture/account/password_reset_confirm.html'), name='password_reset_confirm'
        ),
    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='culture/account/password_reset_complete.html'), name='password_reset_complete'
        ),
    #### Other pages
    path('contribute/', TemplateView.as_view(template_name='culture/contribute.html'), name='contribute'),
    path('features/', TemplateView.as_view(template_name='culture/features.html'), name='features'),
    path('mylist/', TemplateView.as_view(template_name='culture/mylist.html'), name='mylist'),
    path('categories/', TemplateView.as_view(template_name='culture/categories.html'), name='categories'),
    path('productinfo/', TemplateView.as_view(template_name='culture/productinfo.html'), name='productinfo'),
    # path('productinfo/<int:pk>/', views.ProductInfo.as_view(), name='productinfo'),
    path('profile/', TemplateView.as_view(template_name='culture/profile.html'), name='profile'),
    # path('profile/<int:pk>/', views.Profile.as_view(), name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
