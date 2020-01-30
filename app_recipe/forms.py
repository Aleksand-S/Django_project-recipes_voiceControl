from django import forms
from django.contrib.auth.models import User
from prompt_toolkit.validation import ValidationError

from .models import *


class AddRecipeForm(forms.Form):
    recipe_name = forms.CharField(max_length=128)

    main_image = forms.ImageField(required=False)

    cooking_time = forms.TimeField(widget=forms.TimeInput)

    number_of_persons = forms.IntegerField()

    ingredients_object = Ingredient.objects.all()
    ingredients_choises = [(ingredd.ingredient_name, ingredd.ingredient_name) for ingredd in ingredients_object]
    ingredients = forms.ChoiceField(choices=ingredients_choises)

    quantity = forms.DecimalField(min_value=0.01, max_digits=6, decimal_places=2)

    units_object = Unit.objects.all()
    units_choises = [(unit.unit_name, unit.unit_name) for unit in units_object]
    units = forms.ChoiceField(choices=units_choises)

    step_description = forms.CharField(widget=forms.Textarea)

    step_image = forms.ImageField(required=False)


class LoginForm(forms.Form):
    login = forms.CharField(label='Login', max_length=120)
    password = forms.CharField(label='Password', max_length=120, widget=forms.PasswordInput)


def LoginCheck(value):
    is_user_in_DB = User.objects.filter(username=value)
    if len(is_user_in_DB) > 0:
        raise ValidationError('Użytkownik już istneje')


class AddUserForm(forms.Form):
    login = forms.CharField(max_length=20, validators=[LoginCheck])
    password = forms.CharField(max_length=16, widget=forms.PasswordInput())
    repeated_password = forms.CharField(max_length=16, widget=forms.PasswordInput())
    email = forms.EmailField()

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        repeated_password = cleaned_data.get('repeated_password')
        if password != repeated_password:
            raise forms.ValidationError('Hasła są różne!')


class ChangePasswordForm(forms.Form):
    new_password1 = forms.CharField(label='Password', max_length=16, widget=forms.PasswordInput())
    new_password2 = forms.CharField(label='Repeat password', max_length=16, widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        new_password1 = cleaned_data.get('new_password1')
        new_password2 = cleaned_data.get('new_password2')
        if new_password1 != new_password2:
            raise forms.ValidationError('Hasła są różne!')
