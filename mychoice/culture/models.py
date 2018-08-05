"""All the models for the culture app of mychoice project."""


# Standard library imports
#####

# Django imports
# from django.conf import settings
from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    """To create the Category table in the database with 4 choices as category name."""
    CATEGORY_NAME = (
        ('L', 'Livres'),
        ('F', 'Films'),
        ('S', 'Séries'),
        ('M', 'Musique'),
        )
    name = models.CharField("catégorie", max_length=1, choices=CATEGORY_NAME)

    class Meta:
        verbose_name = "catégorie"

    def __str__(self):
        return self.name


class Recommandation(models.Model):
    """To create the Recommandation table in the database which stores
    the recommandation of cultural products of each user."""
    comment = models.TextField("commentaires")
    date = models.DateTimeField("date", auto_now=True)

    class Meta:
        verbose_name = "commentaires"

    def __str__(self):
        return self.comment


class CulturalProduct(models.Model):
    """To create the CulturalProduct table in the database with 8 attributs (fields)."""
    title = models.CharField("titre", max_length=100)
    author = models.CharField("auteur", max_length=100, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='category', verbose_name="catégorie")
    director = models.CharField("réalisateur", max_length=100, blank=True)
    editor = models.CharField("éditeur", max_length=100, blank=True)
    collection = models.CharField("collection", max_length=100, blank=True)
    price = models.DecimalField("prix", max_digits=5, decimal_places=2, null=True)
    isbn = models.CharField("isbn", max_length=20, blank=True)
    year = models.SmallIntegerField("année")
    genre = models.CharField("genre", max_length=30, blank=True)
    nationality = models.CharField("nationalité", max_length=20, blank=True)
    pages = models.SmallIntegerField("pages", null=True)
    language = models.CharField("langue", max_length=30, blank=True)
    label = models.CharField("genre", max_length=30, blank=True)
    image = models.ImageField("image du produit")
    recommandation = models.ForeignKey(
        Recommandation, on_delete=models.CASCADE, related_name='recommandation', verbose_name="recommandation")

    class Meta:
        verbose_name = "produit culturel"

    def __str__(self):
        return '%s %s' % (self.title)


class MyList(models.Model):
    """To create the MyList table in the database which stores
    the list of cultural products for each user."""
    setting = models.DateTimeField("date", auto_now=True)
    cultural_product = models.ManyToManyField(
        CulturalProduct, related_name='cultural_product_selected', verbose_name="porduit culturel sélectionné")

    class Meta:
        verbose_name = "ma liste"

    def __str__(self):
        return self.cultural_product


class Notification(models.Model):
    """To create the Notification table in the database which stores
    the notification of each user."""
    setting = models.DateTimeField("date", auto_now=True)
    category_to_follow = models.ManyToManyField(
        Category, related_name='category_to_follow', verbose_name="catégories à suivre")

    class Meta:
        verbose_name = "notification"

    def __str__(self):
        return self.category_to_follow


class UserProfile(models.Model):
    """To create the ...."""
    GENDER = (
        ('M', 'Masculin'),
        ('F', 'Féminin'),
        )
    AGE_BRACKET = (
        ('1', 'Moins de 18 ans'),
        ('2', 'De 18 à 25 ans'),
        ('3', 'De 26 à 35 ans'),
        ('4', 'De 36 à 45 ans'),
        ('5', 'De 46 à 59 ans'),
        ('6', 'De 60 à 75 ans'),
        ('7', 'Plus de 75 ans'),
        )
    REGION = (
        ('FR-ARA', 'Auvergne-Rhône-Alpes'),
        ('FR-BFC', 'Bourgogne-Franche-Comté'),
        ('FR-BRE', 'Bretagne'),
        ('FR-CVL', 'Centre-Val de Loire'),
        ('FR-COR', 'Corse'),
        ('FR-GES', 'Grand Est'),
        ('FR-HDF', 'Hauts-de-France'),
        ('FR-IDF', 'Île-de-France'),
        ('FR-NOR', 'Normandie'),
        ('FR-NAQ', 'Nouvelle-Aquitaine'),
        ('FR-OCC', 'Occitanie'),
        ('FR-PDL', 'Pays de la Loire'),
        ('FR-PAC', 'Provence-Alpes-Côte d\'Azur'),
        ('FR-GP', 'Guadeloupe'),
        ('FR-GF', 'Guyane'),
        ('FR-MQ', 'Martinique'),
        ('FR-RE', 'La Réunion'),
        ('FR-YT', 'Mayotte'),
        ('FR-TOM', 'Territoires d\'outre-mer'),
        ('EUROPE', 'Europe'),
        ('MONDE', 'Reste du monde'),
        )
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # username = models.CharField("utilisateur", max_length=50)
    # email = models.EmailField("email", max_length=100)
    # password = models.CharField("mot de passe", max_length=30)
    gender = models.CharField("catégorie", max_length=1, choices=GENDER)
    age = models.CharField("catégorie", max_length=1, choices=AGE_BRACKET)
    region = models.CharField("catégorie", max_length=6, choices=REGION)
    photo = models.ImageField("photo", upload_to='profile_photo', blank=True)
    presentation = models.TextField("presentation", blank=True)
    mylist = models.ForeignKey(
        MyList, on_delete=models.CASCADE, related_name='liste', verbose_name="liste")
    notification = models.ForeignKey(
        Notification, on_delete=models.CASCADE, related_name='notification', verbose_name="notification")

    class Meta:
        verbose_name = "utilisateur"

    def __str__(self):
        return self.user
