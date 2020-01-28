from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView
from django.urls import reverse_lazy
from app_recipe.forms import *
from app_recipe.models import *


class MainView(View):
    def get(self, request):
        return HttpResponse('Test index')


class AddIngredientView(CreateView):
    model = Ingredient
    fields = ['ingredient_name', 'calories']
    success_url = reverse_lazy('index')


class AddUnitView(CreateView):
    model = Unit
    fields = ['unit_name']
    success_url = reverse_lazy('index')


class AddRecipeView(View):
    def get(self, request):
        form = AddRecipeForm()
        return render(request, 'app_recipe/add_recipe.html', {'form':form, 'submit_value':'Dodaj do DB'})

    def post(self, request):
        form = AddRecipeForm(request.POST, request.FILES)

        if form.is_valid():

            # constant_block
            name = form.cleaned_data['recipe_name']
            main_image = form.cleaned_data['main_image']
            cooking_time = form.cleaned_data['cooking_time']
            number_of_persons = form.cleaned_data['number_of_persons']

            # ingredients_block, all in arrays
            ingredients = request.POST.getlist('ingredients')
            quantity = request.POST.getlist('quantity')
            units = request.POST.getlist('units')

            # arrays of objects from DB
            ingredients_array = [Ingredient.objects.get(ingredient_name=ingredient) for ingredient in ingredients]
            unit_array = [Unit.objects.get(unit_name=unit) for unit in units]


            recipe_object = Recipe.objects.create(recipe_name=name, main_image=main_image,
                                                  cooking_time=cooking_time, number_of_persons=number_of_persons)

            for index, ingredient in enumerate(ingredients_array):
                recipe_ingredient_quantity_unit_object = RecipeIngredientQuantityUnit()
                recipe_ingredient_quantity_unit_object.recipe = recipe_object
                recipe_ingredient_quantity_unit_object.ingredient = ingredient
                recipe_ingredient_quantity_unit_object.quantity = quantity[index]
                recipe_ingredient_quantity_unit_object.unit = unit_array[index]
                recipe_ingredient_quantity_unit_object.save()

            return HttpResponse('OK')

        return render(request, 'app_recipe/add_recipe.html', {'form':form})


class allRecipesView(View):
    def get(self, request):
        pass


class RecipeByIdView(View):
    def get(self, request):
        pass
