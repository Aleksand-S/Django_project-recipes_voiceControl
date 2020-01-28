from django import forms
from .models import *


class AddRecipeForm(forms.Form):
    recipe_name = forms.CharField(max_length=128, label='Name')

    main_image = forms.ImageField()

    cooking_time = forms.TimeField(widget=forms.TimeInput)

    number_of_persons = forms.IntegerField()

    ingredients_object = Ingredient.objects.all()
    ingredients_choises = [(ingredd.ingredient_name, ingredd.ingredient_name) for ingredd in ingredients_object]
    ingredients = forms.ChoiceField(choices=ingredients_choises)

    quantity = forms.DecimalField(min_value=0.01, max_digits=6, decimal_places=2)

    units_object = Unit.objects.all()
    units_choises = [(unit.unit_name, unit.unit_name) for unit in units_object]
    units = forms.ChoiceField(choices=units_choises)
