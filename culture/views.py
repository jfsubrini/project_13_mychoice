"""All the views for the culture app of mychoice project."""


# # Django imports
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required
# from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# from django.shortcuts import render, redirect, reverse
# from django.views.generic.detail import DetailView
# from django.http import Http404


# # Imports from my app
# from .models import Recommandation
# # from .forms import AccountForm



####### REGISTER #######
def register(request):
    """View to the user register page and validation of the user form."""
    # Analysis and treatment of the register form that has been sent.
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            gender = form.cleaned_data['gender']
            age = form.cleaned_data['age']
            region = form.cleaned_data['region']
            presentation = form.cleaned_data['presentation']
            photo = form.cleaned_data['photo']
            user = User.objects.create_user(
                username, email, password, gender, age, region, presentation, photo)
            user = authenticate(request, username=username, email=email, password=password)
            # If data are valid, automatic log in and redirection to 'Mon Compte' page.
            login(request, user)
            return redirect('account')
    else:
        form = AccountForm()

    # What to render to the template.
    context = {
        'form': form,
        'errors': form.errors.items()
        }
    return render(request, 'food/account/register.html', context)









# ####### PAGE D'INFORMATION SUR UN PRODUIT CULTUREL RECOMMANDE #######
# class ProductInfo(DetailView):
#     """ Generic View for the productinfo page. """
#     context_object_name = "product_info"
#     model = Recommandation
#     template_name = "culture/productinfo.html"


# ####### PAGE DE PROFIL DES CONTRIBUTEURS #######
# class Profile(DetailView):
#     """ Generic View for the profile page. """
#     context_object_name = "profile"
#     model = User
#     template_name = "culture/profile.html"


    # AGE_BRACKET = (
    #     ('1', 'Moins de 18 ans'),
    #     ('2', 'De 18 à 25 ans'),
    #     ('3', 'De 26 à 35 ans'),
    #     ('4', 'De 36 à 45 ans'),
    #     ('5', 'De 46 à 59 ans'),
    #     ('6', 'De 60 à 75 ans'),
    #     ('7', 'Plus de 75 ans'),
    #     )


