from django import forms
from .models import *


class AddRecipeForm(forms.Form):
    recipe_name = forms.CharField(max_length=128, label='Name')
    ingredients_object = Ingredient.objects.all()
    ingredients_choises = [(ingredd.ingredient_name, ingredd.ingredient_name) for ingredd in ingredients_object]
    ingredients = forms.ChoiceField(choices=ingredients_choises)
