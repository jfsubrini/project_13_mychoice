"""All the models for the culture app of mychoice project."""


# Standard library imports
# from enumchoicefield import ChoiceEnum, EnumChoiceField

# Django imports
from django.conf import settings
from django.db import models



# class CategoryName(ChoiceEnum):
#     """ENUM values for name in the Category model."""
#     1 = "Livres"
#     2 = "Films"
#     3 = "Séries"
#     4 = "Musique"


# class Region(ChoiceEnum):
#     """ENUM values for region in the User model."""
#     1 = "Auvergne-Rhône-Alpes"
#     2 = "Bourgogne-Franche-Comté"
#     3 = "Bretagne"
#     4 = "Centre-Val de Loire"
#     5 = "Corse"
#     6 = "Grand Est"
#     7 = "Hauts-de-France"
#     8 = "Normandie"
#     9 = "Nouvelle-Aquitaine"
#     10 = "Occitanie"
#     11 = "Pays de la Loire"
#     12 = "Provence-Alpes-Côte d'Azur"
#     13 = "Guadeloupe"
#     14 = "Guyane"
#     15 = "Martinique"
#     16 = "La Réunion"
#     17 = "Mayotte"
#     18 = "Territoires d'outre-mer"
#     19 = "Europe"
#     20 = "Reste du monde"


# class Age(ChoiceEnum):
#     """ENUM values for age in the User model."""
#     1 = "Moins de 18 ans"
#     2 = "De 18 à 25 ans"
#     3 = "De 26 à 35 ans"
#     4 = "De 36 à 45 ans"
#     5 = "De 46 à 59 ans"
#     6 = "De 60 à 75 ans"
#     7 = "Plus de 75 ans"


# class Gender(ChoiceEnum):
#     """ENUM values for gender in the User model."""
#     customRadio1 = "Masculin"
#     customRadio2 = "Féminin"


class Category(models.Model):
    """To create the Category table in the database."""
    # name = EnumChoiceField(CategoryName, verbose_name="nom")
    name = models.CharField("catégorie", max_length=255) ## FAUX

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
    # image = models.############)
    recommandation = models.ForeignKey(
        Recommandation, on_delete=models.CASCADE, related_name='recommandation', verbose_name="recommandation")

    # image_food = models.URLField("url de l'image de l'aliment")

    class Meta:
        verbose_name = "produit culturel"

    def __str__(self):
        return '%s %s' % (self.title)


class Notification(models.Model):
    """To create the Notification table in the database which stores
    the notification of each user."""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category_to_follow = models.ManyToManyField(
        Category, related_name='category_to_follow', verbose_name="catégories à suivre")

    class Meta:
        verbose_name = "notification"

    def __str__(self):
        return self.user


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
