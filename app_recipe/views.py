from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import CreateView
from django.urls import reverse_lazy
from app_recipe.forms import *
from app_recipe.models import *
from app_recipe.voice import start_voice_assistant
import threading


class MainView(View):
    def get(self, request):
        all_recipes = Recipe.objects.all().order_by('-pk')[:3]
        return render(request, 'app_recipe/index.html', {'recipes':all_recipes})


class AddIngredientView(CreateView):
    model = Ingredient
    fields = ['ingredient_name', 'calories']
    success_url = reverse_lazy('index')


class AddUnitView(CreateView):
    model = Unit
    fields = ['unit_name']
    success_url = reverse_lazy('index')


class AddRecipeView(PermissionRequiredMixin, View):
    permission_required = 'app_recipe.add_recipe'

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

            # steps block, all in arrays
            description = request.POST.getlist('step_description')
            step_image = request.FILES.getlist('step_image')

            # arrays of objects from DB
            ingredients_array = [Ingredient.objects.get(ingredient_name=ingredient) for ingredient in ingredients]
            unit_array = [Unit.objects.get(unit_name=unit) for unit in units]

            recipe_object = Recipe.objects.create(recipe_name=name, main_image=main_image,
                                                  cooking_time=cooking_time, number_of_persons=number_of_persons)
            # add ingredients to DB
            for index, ingredient in enumerate(ingredients_array):
                recipe_ingredient_quantity_unit_object = RecipeIngredientQuantityUnit()
                recipe_ingredient_quantity_unit_object.recipe = recipe_object
                recipe_ingredient_quantity_unit_object.ingredient = ingredient
                recipe_ingredient_quantity_unit_object.quantity = quantity[index]
                recipe_ingredient_quantity_unit_object.unit = unit_array[index]
                recipe_ingredient_quantity_unit_object.save()

            # add steps to DB
            for index in range(len(description)):
                Step.objects.create(recipe=recipe_object, description=description[index],
                                    step_image=step_image[index])

            return HttpResponse('OK')

        return render(request, 'app_recipe/add_recipe.html', {'form':form})


class RecipeByIdView(View):
    def get(self, request, recipe_id):
        recipe_obj = get_object_or_404(Recipe, pk=recipe_id)
        array_steps_to_voice = [element.description for element in recipe_obj.step_set.all().order_by('pk')]
        try:
            print('Try to ON mic')
            # start_voice_assistant(array_steps_to_voice)
            asynch_process = threading.Thread(target=start_voice_assistant, args=(array_steps_to_voice,))
            asynch_process.start()
            print('try to ON asynch process')
        finally:
            print('all errors after voice')
        print('Try to ON mic')
        return render(request, 'app_recipe/recipe_by_id.html', {'recipe_obj': recipe_obj})


# Empty -------------------------------------------------------!!!!!
class allRecipesView(View):
    def get(self, request):
        pass
# --------------------------------------------------------------

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'app_recipe/form.html', {'form': form, 'submit_value':'Login'})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['login']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                return render(request, 'app_recipe/form.html', {'form': form, 'info': 'Błędny login lub hasło', 'submit_value':'Login'})
        else:
            return render(request, 'app_recipe/form.html', {'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')


class AddUserView(View):
    def get(self, request):
        form = AddUserForm()
        return render(request, 'app_recipe/form.html', {'form':form})

    def post(self, request):
        form = AddUserForm(request.POST)

        if form.is_valid():
            users_login = form.cleaned_data['login']
            first_password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            new_user = User(username=users_login, email=email)
            new_user.set_password(first_password)
            new_user.save()
            return redirect('index')

        else:
            return render(request, 'app_recipe/form.html', {'form': form})


class ChangePasswordView(PermissionRequiredMixin, View):
    permission_required = 'app_recipe.change_password'

    def get(self, request, user_id):
        form = ChangePasswordForm
        return render(request, 'app_recipe/form.html', {'form': form})

    def post(self, request, user_id):
        form = ChangePasswordForm(request.POST)
        user = get_object_or_404(User, pk=user_id)
        if form.is_valid():
            new_password = form.cleaned_data['new_password1']
            user.set_password(new_password)
            user.save()
            return HttpResponse('Zmiana hasła')
        else:
            return render(request, 'app_recipe/form.html', {'form': form})