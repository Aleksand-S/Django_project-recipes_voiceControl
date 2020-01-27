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

class AddRecipeView(View):
    def get(self, request):
        form = AddRecipeForm()
        return render(request, 'app_recipe/form.html', {'form':form, 'submit_value':'Dodaj do DB'})

    def post(self, request):
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            name = form.data['recipe_name']
            ingredients = request.POST.getlist('ingredients')

            # цикл возвращаем ключ из БД и дописываем ключ в ингридиенты рецепта
            ingredients_array = []
            for ingredient in ingredients:
                ingredient_obj = Ingredient.objects.get(ingredient_name=ingredient)
                ingredients_array.append(ingredient_obj)
            obj_add_to_db = Recipe.objects.create(recipe_name=name)
            obj_add_to_db.ingredients.add(*ingredients_array)
            obj_add_to_db.save()
            # --------------------------------------------------------------------

        return HttpResponse('OK')

