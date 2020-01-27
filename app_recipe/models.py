from django.db import models

# Create your models here.

class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=128)
    calories = models.IntegerField(null=True)


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=128)
    ingredients = models.ManyToManyField(Ingredient)
