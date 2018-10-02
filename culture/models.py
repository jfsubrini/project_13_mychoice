"""All the models for the culture app of mychoice project."""


# Django imports
from django.db import models
from django.contrib.auth.models import User



class UserProfile(models.Model):
    """To create the extension of the Django User model to add more data of the user profile."""
    GENDER = (
        ('M', 'Masculin'),
        ('F', 'Féminin'),
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
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="utilisateur")
    gender = models.CharField("genre", max_length=1, choices=GENDER)
    age = models.DateField("âge")
    region = models.CharField("région", max_length=6, choices=REGION)
    photo = models.ImageField("photo du profil", upload_to='profile_photo/%d/%m/%Y/', null=True)
    presentation = models.TextField("présentation", blank=True)

    class Meta:
        verbose_name = "utilisateur"

    def __str__(self):
        return self.user


class Category(models.Model):
    """To create the Category table in the database with 4 choices as category name."""
    CATEGORY_NAME = (
        ('L', 'Livres'),
        ('F', 'Films'),
        ('S', 'Séries'),
        ('M', 'Musique'),
        )
    name = models.CharField("nom de la catégorie", max_length=1, choices=CATEGORY_NAME)

    class Meta:
        verbose_name = "catégorie"

    def __str__(self):
        return self.name


class CulturalProduct(models.Model):
    """To create the CulturalProduct table in the database with various attributs (fields)."""
    title = models.CharField("titre", max_length=100)
    author_director = models.CharField("auteur ou réalisateur", max_length=100)
    editor_label = models.CharField("éditeur ou label", max_length=100)
    year = models.SmallIntegerField("année")
    image = models.ImageField("image du produit", upload_to='product_image/')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='cultural_product', \
        verbose_name="catégorie")
    collection = models.CharField("collection", max_length=100, blank=True)
    price = models.DecimalField("prix", max_digits=5, decimal_places=2, null=True)
    isbn = models.CharField("isbn-13", max_length=20, blank=True)
    genre = models.CharField(max_length=30, blank=True)
    nationality = models.CharField("nationalité", max_length=20, blank=True)
    pages = models.SmallIntegerField(null=True)
    language = models.CharField("langue", max_length=30, blank=True)

    class Meta:
        verbose_name = "titre du produit culturel"

    def __str__(self):
        return self.title


class MyList(models.Model):
    """To create the MyList table in the database which stores the user's selection
    of cultural products."""
    setting = models.DateTimeField("date de création", auto_now=True)
    user_profile = models.OneToOneField(
        UserProfile, on_delete=models.CASCADE, related_name='list_of', \
        verbose_name="utilisateur")
    cultural_products = models.ManyToManyField(
        CulturalProduct, related_name='list_of',\
        verbose_name="porduit culturel sélectionné")

    class Meta:
        verbose_name = "ma liste"

    def __str__(self):
        return self.user_profile


class Notification(models.Model):
    """To create the Notification table in the database which stores
    the notification scheme of each user."""
    setting = models.DateTimeField("date de création", auto_now=True)
    categories = models.ManyToManyField(
        Category, related_name='notification_of', verbose_name="catégorie(s) à suivre")
    user_profile = models.OneToOneField(
        UserProfile, on_delete=models.CASCADE, related_name='notification_of', \
        verbose_name="utilisateur")

    class Meta:
        verbose_name = "notification"

    def __str__(self):
        return self.categories


class Recommendation(models.Model):
    """To create the Recommendation table in the database which stores
    the recommendation of cultural products from each user."""
    comment = models.TextField("commentaires sur le produit culturel")
    date = models.DateTimeField("date de création", auto_now=True)
    user_profile = models.ManyToManyField(
        UserProfile, related_name='recommendation_text', \
        verbose_name="utilisateur")
    cultural_product = models.ManyToManyField(
        CulturalProduct, related_name='recommendation_text',\
        verbose_name="produit culturel")

    class Meta:
        verbose_name = "produit recommandé"

    def __str__(self):
        return self.cultural_product
