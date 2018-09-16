"""Creation of the user account form."""


# Django imports
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput
from django.contrib.auth.models import User



class AccountForm(ModelForm):
    """Form to create the user register account, based on the Django User model."""

    class Meta:
        """Details of the register form and attributes settings for CSS."""
        model = UserProfile
        fields = ['username', 'email', 'password', 'gender', 'age', \
        'region', 'photo', 'presentation']
        widgets = {
            'username': TextInput(attrs={'class': 'form-control', 'type': 'text', \
                'name': 'placeholder', 'placeholder': 'Entrez votre nom d\'utilisateur'}),
            'email': EmailInput(attrs={'class': 'form-control', 'id': 'email', \
                'name': 'email', 'type': 'text', 'placeholder': 'Entrez votre email', 'required': 'required'}),
            'password': PasswordInput(attrs={'class': 'form-control', 'type': 'password' \
                'name': 'pass', 'placeholder': 'Entrez votre mot de passe'}),
            # 'gender': RADIO(attrs={'class': 'custom-control-input', 'type': 'radio', \
            #     'id': 'customRadio2', 'name': 'customRadio'}),
            # 'age': SELECT(attrs={'class': 'custom-select form-control', \
            #     .................}),
            # 'region': SELECT(attrs={'class': 'custom-select form-control', \
            #     .................}),
            # 'photo': ................,
            # 'presentation': TEXTAREA(attrs={'class': 'form-control', 'name': 'message', \
            #     'id': 'message', 'rows': '10', \
            #     'placeholder': 'Ecrivez un petit texte décrivant vos passions et votre intérêt pour la culture.'})
        }
