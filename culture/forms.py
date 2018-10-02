"""Creation of the user account form."""


# Django imports
from django.forms import ModelForm
from .models import UserProfile



class AccountForm(ModelForm):
    """Form to create the user register account, based on the Django User model."""

    class Meta:
        """Details of the register form and attributes settings for CSS."""
        model = UserProfile
        fields = ['username', 'email', 'password', 'gender', 'age', 'region', \
        'photo', 'presentation']
