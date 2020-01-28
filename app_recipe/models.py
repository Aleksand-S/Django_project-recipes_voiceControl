from django.db import models

# Create your models here.

class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=128)
    calories = models.IntegerField(null=True)


class Unit(models.Model):
    unit_name = models.CharField(max_length=64)


class Category(models.Model):  # while skipping
    category_name = models.CharField(max_length=64)


class Cuisine(models.Model):  # while skipping
    cuisine_name = models.CharField(max_length=64)


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=128)
    main_image = models.ImageField(upload_to='images/', blank=True)
    ingredients = models.ManyToManyField(Ingredient, through="RecipeIngredientQuantityUnit")
    # quantity = models.IntegerField(null=True)  # redirected to model RecipeIngredientQuantityUnit
    # units = models.ForeignKey(Unit, on_delete=models.CASCADE, null=True)  # redirected to model RecipeIngredientQuantityUnit
    cooking_time = models.TimeField(null=True)
    number_of_persons = models.IntegerField(null=True)
    categories = models.ManyToManyField(Category)  # while skipping
    cuisines = models.ManyToManyField(Cuisine)  # while skipping
    recipe_date = models.DateTimeField(auto_now_add=True, null=True)
    rating = models.IntegerField(default=0)
    # steps = models.ForeignKey(Step, on_delete=models.CASCADE, null=True)


class RecipeIngredientQuantityUnit(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)


# class Step(models.Model):
#     recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
#     step_number = models.IntegerField()
#     description = models.TextField()
#     step_image = models.ImageField(upload_to='images/', blank=True)


# class Comment(models.Model):
#     from_user = models.ForeignKey(User, on_delete=models.CASCADE)  # в какой класс??
#     to_recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
#     comment_content = models.TextField()
#     comment_date = models.DateTimeField(auto_now_add=True)


# class Rating(models.Model):
#     rating_points = models.IntegerField()
#     users = models.ForeignKey(User, on_delete=models.CASCADE)
#     recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
