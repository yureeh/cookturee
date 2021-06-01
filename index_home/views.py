from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Recipe, Heart, Statistics, Ingredients, checked_insert, Unit, UnitRatio, Tags, Post, \
    ReceIngres, Step, recipe_skill, recipe_tool, recipe_scheduling, Category, Skill, Tool, ReceIngres2, TempRecipes, \
    TempHearts, User_Recipe, No_Recipe, No_Users, No_Categories, No_Ingres, No_Skills, No_Tools, No_Tags, No_Units, \
    No_Submitted, No_Featured, Logs_recipes
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib import messages
import pandas as pd  # high-level data manipulation tool
import numpy as np  # provides a high-performance multidimensional array object, and tools for working with these arrays
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
# Import linear_kernel
from sklearn.metrics.pairwise import linear_kernel
from .forms import MyForm, HotelForm, CreateRecipe, CreateIngredient, CreatePreparation, CreateSkill, CreateTool, \
    CreateCategory, CreateIngredients, CreateSkills, CreateTools, CreateTags, CreateUnits, CreateSchedule, \
    CreateIngredient2, CreateRecipe2
from . import hybrid
from django.urls import reverse
from .filters import RecipesFilter
from django.contrib import messages

# Create your views here.
# def Filtered_recipe(ListView):
#     model = Recipe
#     template_name = 'index_home/filtered_recipe.html'
#     context_object_name = 'recipe'


def home(request):
    context = {
        "Total_Recipe": No_Recipe.objects.first(),
        "Total_Users": No_Users.objects.first(),
        "Total_Categories": No_Categories.objects.first(),
        "Total_Ingres": No_Ingres.objects.first(),
        "Total_Skills": No_Skills.objects.first(),
        "Total_Tools": No_Tools.objects.first(),
        "Total_Tags": No_Tags.objects.first(),
        "Total_Units": No_Units.objects.first(),
        "Total_Submitted": No_Submitted.objects.first(),
    }
    return render(request, 'index_home/home.html', context)


def admin_home(request):
    context = {
        "Total_Recipe": No_Recipe.objects.first(),
        "Total_Users": No_Users.objects.first(),
        "Total_Categories": No_Categories.objects.first(),
        "Total_Ingres": No_Ingres.objects.first(),
        "Total_Skills": No_Skills.objects.first(),
        "Total_Tools": No_Tools.objects.first(),
        "Total_Tags": No_Tags.objects.first(),
        "Total_Units": No_Units.objects.first(),
        "Total_Submitted": No_Submitted.objects.first(),
        'recipes': Recipe.objects.order_by('date_added'),
        'recipes_featured': No_Featured.objects.order_by('-total_hearts')[:10],
        "ree": hybrid.featured_recipes,
    }
    return render(request, 'index_home/dashboard.html', context)


def packages(request):
    context = {
        'Recipes': Recipe.objects.all(),
        'title': 'Packages',
        'Users': User.objects.all(),
    }
    return render(request, 'index_home/packages.html', context)


def help(request):
    context = {
        'Ingres': ReceIngres.objects.all(),
        'Steps': Step.objects.all(),
    }
    return render(request, 'index_home/help.html', context)


def blog(request):
    content = {
        'ree': No_Featured.objects.order_by('-date_added'),
        'title': 'Blog'
    }
    return render(request, 'index_home/help.html', content)


class RecipeListView(ListView):
    model = No_Featured
    template_name = 'index_home/blog.html'
    context_object_name = 'recipes'
    ordering = ['-total_hearts']

    def get_context_data(self, **kwargs):
        context = super(RecipeListView, self).get_context_data(**kwargs)
        context['filter'] = RecipesFilter(self.request.GET, queryset=self.get_queryset())
        return context


class RecipeListViewBase(ListView):
    model = Recipe
    template_name = 'index_home/base.html'
    context_object_name = 'recipes'
    ordering = ['-date_added']


class UserRecipeListView(ListView):
    model = Recipe
    template_name = 'index_home/user_recipe.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Recipe.objects.filter(author=user).order_by('-date_added')


class RecipeDetailView(DetailView):
    model = Recipe

    # model_2 = Recipe.objects.filter('recepingre')

    def get_queryset(self):
        return self.model.objects.order_by('-date_added')

    def get_context_data(self, **kwargs):
        context = super(RecipeDetailView, self).get_context_data(**kwargs)
        context['Ingredients'] = ReceIngres.objects.all()
        context['Steps'] = Step.objects.order_by("order")
        context['Recipes_info'] = Recipe.objects.order_by("-date_added")
        context['Skills'] = recipe_skill.objects.all()
        context['Tools'] = recipe_tool.objects.all()

        stuff = get_object_or_404(Recipe, id=self.kwargs['pk'])
        total_hearts = stuff.total_hearts()

        liked = False
        if stuff.hearts.filter(id=self.request.user.id).exists():
            liked = True

        context['total_hearts'] = total_hearts
        context['like'] = liked
        return context


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = CreateRecipe

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, f'Recipe Successfully Created!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(RecipeCreateView, self).get_context_data(**kwargs)
        context['Ingredients'] = ReceIngres.objects.all()
        return context


class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    # fields = ['name', 'photo', 'description']
    form_class = CreateRecipe

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, f'Recipe Successfully Updated!')
        return super().form_valid(form)

    def test_func(self):
        recipe = self.get_object()
        if self.request.user == recipe.author:
            return True
        return False


class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    success_url = '/'

    def test_func(self):
        recipe = self.get_object()
        if self.request.user == recipe.author:
            return True
        return False


class RecipeIngredientView(CreateView):
    model = ReceIngres
    form_class = CreateIngredient

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, f'Successfully Added!')
        return super().form_valid(form)

    def test_func(self):
        recipe = self.get_object()
        if self.request.user == recipe.recipe.author:
            return True
        return False


def contact(request):
    return render(request, 'index_home/contact.html', {'title': 'Contact'})


def add(request):
    val1 = request.GET['key']
    hybrid_result = hybrid.hybrid(val1)
    isexist = hybrid.isKeyExist(val1)
    context = {
        'result': val1,
        'recipes': No_Featured.objects.order_by('-total_hearts'),
        'ids':  hybrid_result[1],
        'remark': isexist[0],
        'ree': isexist[1],
        'oras': hybrid_result[2],
        # 'Ingredients': ReceIngres.objects.all(),
        # 'ree': hybrid.hybrid(val1).to_html(),
        # "hearts": TempHearts.objects.all(),
    }
    return render(request, 'index_home/result.html', context)


def basket(request):
    form = MyForm(request.POST or None)
    name = ''
    if request.method == "POST":
        if form.is_valid():
            ...
            if request.POST["something_truthy"]:
                name = request.POST["something_truthy"]
                ...
    # This will display the blank form for a GET request
    # or show the errors on a POSTed form that was invalid
    # return render(request, 'your_template.html', {'form': form})
    context = {
        'ingredients': Ingredients.objects.order_by('name'),
        'Recipes_info': Recipe.objects.order_by('-date_added'),
        'form': form,
        'testing': name,
    }
    return render(request, 'index_home/basket.html', context)


def unit_converter(request):
    content = {
        'recipes': Recipe.objects.order_by('-date_added'),
        'units': Unit.objects.all(),
    }
    return render(request, 'index_home/unit_converter.html', content)


def createpost(request):
    if request.method == 'POST':
        if request.POST["title"] and request.POST["content"]:
            post = Post()
            post.title = request.POST["title"]
            post.content = request.POST["content"]
            post.save()

            return render(request, 'index_home/create.html')

    else:
        return render(request, 'index_home/create.html')


# Create your views here.
def hotel_image_view(request):
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)
        if request.POST["title"] and request.POST["content"]:
            post = Post()
            post.title = request.POST["title"]
            post.content = request.POST["content"]
            post.save()

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = HotelForm()
    context = {
        'form': form,
    }
    return render(request, 'index_home/create.html', context)


def success(request):
    return HttpResponse('successfully uploaded')


def testing(request):
    scale = 0
    if request.method == 'POST':
        scale = request.POST["scale_no"]
    context = {
        'scale': scale
    }
    return render(request, 'index_home/recipe_detail.html', context)


def create_recipe(request):
    if request.method == 'POST':
        recipe = CreateRecipe(request.POST, request.FILES)
        ingres = CreateIngredient(request.POST)
        step = CreatePreparation(request.POST)
        skill = CreateSkill(request.POST)
        tool = CreateTool(request.POST)

        if recipe.is_valid():
            recipe.instance.author = request.user
            recipe.save()
            ingres.instance.author = request.user
            # ingres.save()
            step.instance.author = request.user
            # step.save()
            skill.instance.author = request.user
            # skill.save()
            tool.instance.author = request.user
            # tool.save()
            return redirect('recipe-ingre', pk=recipe.id)

    else:
        recipe = CreateRecipe()
        ingres = CreateIngredient()
        step = CreatePreparation()
        skill = CreateSkill()
        tool = CreateTool()
    context = {
        'recipe': recipe,
        'ingres': ingres,
        'step': step,
        'skill': skill,
        'tool': tool,
    }
    return render(request, 'index_home/recipe_form.html', context)


class UsersListView(LoginRequiredMixin, ListView):
    model = User
    context_object_name = 'people'
    template_name = 'index_home/admin_users.html'
    ordering = ['-username']

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super(UsersListView, self).get_context_data(**kwargs)
        context['total'] = No_Users.objects.first()
        context['Total_Recipe'] = No_Recipe.objects.first()
        context['Total_Users'] = No_Users.objects.first()
        context['Total_Categories'] = No_Categories.objects.first()
        context['Total_Ingres'] = No_Ingres.objects.first()
        context['Total_Skills'] = No_Skills.objects.first()
        context['Total_Tools'] = No_Tools.objects.first()
        context['Total_Tags'] = No_Tags.objects.first()
        context['Total_Units'] = No_Units.objects.first()
        return context


class AdminCategoriesListView(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'index_home/admin_categories.html'
    ordering = ['-category']

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super(AdminCategoriesListView, self).get_context_data(**kwargs)
        context['total'] = No_Categories.objects.first()
        context['Total_Recipe'] = No_Recipe.objects.first()
        context['Total_Users'] = No_Users.objects.first()
        context['Total_Categories'] = No_Categories.objects.first()
        context['Total_Ingres'] = No_Ingres.objects.first()
        context['Total_Skills'] = No_Skills.objects.first()
        context['Total_Tools'] = No_Tools.objects.first()
        context['Total_Tags'] = No_Tags.objects.first()
        context['Total_Units'] = No_Units.objects.first()
        return context


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CreateCategory

    def form_valid(self, form):
        messages.success(self.request, f'Successfully Added!')
        return super().form_valid(form)


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CreateCategory

    def form_valid(self, form):
        messages.success(self.request, f'Successfully Updated!')
        return super().form_valid(form)


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    form_class = CreateCategory
    success_url = '/admins/categories'


class AdminIngredientListView(ListView):
    model = Ingredients
    context_object_name = 'ingredients'
    template_name = 'index_home/admin_ingredients.html'
    ordering = ['-category']

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super(AdminIngredientListView, self).get_context_data(**kwargs)
        context['total'] = No_Ingres.objects.first()
        context['Total_Recipe'] = No_Recipe.objects.first()
        context['Total_Users'] = No_Users.objects.first()
        context['Total_Categories'] = No_Categories.objects.first()
        context['Total_Ingres'] = No_Ingres.objects.first()
        context['Total_Skills'] = No_Skills.objects.first()
        context['Total_Tools'] = No_Tools.objects.first()
        context['Total_Tags'] = No_Tags.objects.first()
        context['Total_Units'] = No_Units.objects.first()
        return context


class IngredientCreateView(LoginRequiredMixin, CreateView):
    model = Ingredients
    form_class = CreateIngredients

    def form_valid(self, form):
        messages.success(self.request, f'Successfully Added!')
        return super().form_valid(form)


class IngredientUpdateView(LoginRequiredMixin, UpdateView):
    model = Ingredients
    form_class = CreateIngredients

    def form_valid(self, form):
        messages.success(self.request, f'Successfully Updated!')
        return super().form_valid(form)


class IngredientDeleteView(LoginRequiredMixin, DeleteView):
    model = Ingredients
    form_class = CreateIngredients
    success_url = '/admins/ingredients/'


class AdminSkillsListView(ListView):
    model = Skill
    context_object_name = 'skills'
    template_name = 'index_home/admin_skills.html'
    ordering = ['-skill']

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super(AdminSkillsListView, self).get_context_data(**kwargs)
        context['total'] = No_Skills.objects.first()
        context['Total_Recipe'] = No_Recipe.objects.first()
        context['Total_Users'] = No_Users.objects.first()
        context['Total_Categories'] = No_Categories.objects.first()
        context['Total_Ingres'] = No_Ingres.objects.first()
        context['Total_Skills'] = No_Skills.objects.first()
        context['Total_Tools'] = No_Tools.objects.first()
        context['Total_Tags'] = No_Tags.objects.first()
        context['Total_Units'] = No_Units.objects.first()
        return context


class SkillsCreateView(LoginRequiredMixin, CreateView):
    model = Skill
    form_class = CreateSkills

    def form_valid(self, form):
        messages.success(self.request, f'Successfully Added!')
        return super().form_valid(form)


class SkillsUpdateView(LoginRequiredMixin, UpdateView):
    model = Skill
    form_class = CreateSkills

    def form_valid(self, form):
        messages.success(self.request, f'Successfully Updated!')
        return super().form_valid(form)


class SkillsDeleteView(LoginRequiredMixin, DeleteView):
    model = Skill
    form_class = CreateSkills
    success_url = '/admins/skills/'


class AdminToolsListView(ListView):
    model = Tool
    context_object_name = 'tools'
    template_name = 'index_home/admin_tools.html'
    ordering = ['-tool']

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super(AdminToolsListView, self).get_context_data(**kwargs)
        context['total'] = No_Tools.objects.first()
        context['Total_Recipe'] = No_Recipe.objects.first()
        context['Total_Users'] = No_Users.objects.first()
        context['Total_Categories'] = No_Categories.objects.first()
        context['Total_Ingres'] = No_Ingres.objects.first()
        context['Total_Skills'] = No_Skills.objects.first()
        context['Total_Tools'] = No_Tools.objects.first()
        context['Total_Tags'] = No_Tags.objects.first()
        context['Total_Units'] = No_Units.objects.first()
        return context


class ToolsCreateView(LoginRequiredMixin, CreateView):
    model = Tool
    form_class = CreateTools

    def form_valid(self, form):
        messages.success(self.request, f'Successfully Added!')
        return super().form_valid(form)


class ToolsUpdateView(LoginRequiredMixin, UpdateView):
    model = Tool
    form_class = CreateTools

    def form_valid(self, form):
        messages.success(self.request, f'Successfully Updated!')
        return super().form_valid(form)


class ToolsDeleteView(LoginRequiredMixin, DeleteView):
    model = Tool
    form_class = CreateTools
    success_url = '/admins/tools/'


class AdminTagsListView(ListView):
    model = Tags
    context_object_name = 'tags'
    template_name = 'index_home/admin_tags.html'
    ordering = ['-tool']

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super(AdminTagsListView, self).get_context_data(**kwargs)
        context['total'] = No_Tags.objects.first()
        context['Total_Recipe'] = No_Recipe.objects.first()
        context['Total_Users'] = No_Users.objects.first()
        context['Total_Categories'] = No_Categories.objects.first()
        context['Total_Ingres'] = No_Ingres.objects.first()
        context['Total_Skills'] = No_Skills.objects.first()
        context['Total_Tools'] = No_Tools.objects.first()
        context['Total_Tags'] = No_Tags.objects.first()
        context['Total_Units'] = No_Units.objects.first()
        return context


class TagsCreateView(LoginRequiredMixin, CreateView):
    model = Tags
    form_class = CreateTags

    def form_valid(self, form):
        messages.success(self.request, f'Successfully Added!')
        return super().form_valid(form)


class TagsUpdateView(LoginRequiredMixin, UpdateView):
    model = Tags
    form_class = CreateTags

    def form_valid(self, form):
        messages.success(self.request, f'Successfully Updated!')
        return super().form_valid(form)


class TagsDeleteView(LoginRequiredMixin, DeleteView):
    model = Tags
    form_class = CreateTags
    success_url = '/admins/tags/'


class AdminUnitsListView(ListView):
    model = Unit
    context_object_name = 'units'
    template_name = 'index_home/admin_units.html'
    ordering = ['-unit']

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super(AdminUnitsListView, self).get_context_data(**kwargs)
        context['total'] = No_Units.objects.first()
        context['Total_Recipe'] = No_Recipe.objects.first()
        context['Total_Users'] = No_Users.objects.first()
        context['Total_Categories'] = No_Categories.objects.first()
        context['Total_Ingres'] = No_Ingres.objects.first()
        context['Total_Skills'] = No_Skills.objects.first()
        context['Total_Tools'] = No_Tools.objects.first()
        context['Total_Tags'] = No_Tags.objects.first()
        context['Total_Units'] = No_Units.objects.first()
        return context


class UnitCreateView(LoginRequiredMixin, CreateView):
    model = Unit
    form_class = CreateUnits

    def form_valid(self, form):
        messages.success(self.request, f'Successfully Added!')
        return super().form_valid(form)


class UnitUpdateView(LoginRequiredMixin, UpdateView):
    model = Unit
    form_class = CreateUnits

    def form_valid(self, form):
        messages.success(self.request, f'Successfully Updated!')
        return super().form_valid(form)


class UnitDeleteView(LoginRequiredMixin, DeleteView):
    model = Unit
    form_class = CreateUnits
    success_url = '/admins/units/'


class AdminRecipeListView(ListView):
    model = Recipe
    context_object_name = 'recipes'
    template_name = 'index_home/admin_recipes.html'
    # ordering = ['-privacy']

    def get_queryset(self):
        return self.model.objects.order_by('name')

    def get_context_data(self, **kwargs):
        context = super(AdminRecipeListView, self).get_context_data(**kwargs)
        context['ingres'] = ReceIngres.objects.all()
        context['hearts'] = TempHearts.objects.all()
        context['no_recipes'] = No_Recipe.objects.first()
        context['Total_Recipe'] = No_Recipe.objects.first()
        context['Total_Users'] = No_Users.objects.first()
        context['Total_Categories'] = No_Categories.objects.first()
        context['Total_Ingres'] = No_Ingres.objects.first()
        context['Total_Skill'] = No_Skills.objects.first()
        context['Total_Tools'] = No_Tools.objects.first()
        context['Total_Tags'] = No_Tags.objects.first()
        context['Total_Units'] = No_Units.objects.first()
        return context


class RecipesCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = CreateRecipe2
    template_name = 'index_home/recipes_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, f'Successfully Added!')
        return super().form_valid(form)


class RecipesUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    form_class = CreateRecipe2

    def form_valid(self, form):
        messages.success(self.request, f'Successfully Updated!')
        return super().form_valid(form)


class RecipesDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe
    form_class = CreateRecipe2
    success_url = '/admins/recipes/'


class RecipeIngresCreateView(LoginRequiredMixin, CreateView):
    model = ReceIngres
    form_class = CreateIngredient

    def form_valid(self, form):
        recipe = self.get_object()
        recipeID = get_object_or_404(Recipe, id=recipe.pk)
        form.instance.recipe = recipeID
        messages.success(self.request, f'Successfully Added!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(RecipeIngresCreateView, self).get_context_data(**kwargs)
        return context


class RecipeIngresUpdateView(LoginRequiredMixin, UpdateView):
    model = ReceIngres
    form_class = CreateIngredient

    def form_valid(self, form):
        messages.success(self.request, f'Successfully Updated!')
        return super().form_valid(form)


class RecipeIngresDeleteView(LoginRequiredMixin, DeleteView):
    model = ReceIngres
    form_class = CreateIngredient

    def get_success_url(self):
        return reverse('recipe-detail', kwargs={'pk': self.object.recipe.id})


class PreparationCreateView(LoginRequiredMixin, CreateView):
    model = Step
    form_class = CreatePreparation

    # template_name = 'index_home/step_form.html'

    def form_valid(self, form):
        recipe = self.get_object()
        recipeID = get_object_or_404(Recipe, id=recipe.pk)
        form.instance.recipe = recipeID
        messages.success(self.request, f'Successfully Added!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(PreparationCreateView, self).get_context_data(**kwargs)
        recipe = self.get_object()
        context['ree'] = get_object_or_404(Recipe, id=2)
        return context


class PreparationUpdateView(LoginRequiredMixin, UpdateView):
    model = Step
    form_class = CreatePreparation

    def form_valid(self, form):
        messages.success(self.request, f'Successfully Updated!')
        return super().form_valid(form)


class PreparationDeleteView(LoginRequiredMixin, DeleteView):
    model = Step
    form_class = CreatePreparation

    def get_success_url(self):
        return reverse('recipe-detail', kwargs={'pk': self.object.recipe.id})


class SkillCreateView(LoginRequiredMixin, CreateView):
    model = recipe_skill
    form_class = CreateSkill

    def form_valid(self, form):
        # recipe = self.get_object()
        # recipeID = get_object_or_404(Recipe, id=recipe.pk)
        # form.instance.recipe = recipeID
        messages.success(self.request, f'Successfully Added!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(SkillCreateView, self).get_context_data(**kwargs)
        # recipe = self.get_object()
        # if self.request.user == recipe.recipe.author:
        # context['ree'] = recipe
        return context


class SkillUpdateView(LoginRequiredMixin, UpdateView):
    model = recipe_skill
    form_class = CreateSkill

    def form_valid(self, form):
        messages.success(self.request, f'Successfully Updated!')
        return super().form_valid(form)


class SkillDeleteView(LoginRequiredMixin, DeleteView):
    model = recipe_skill
    form_class = CreateSkill

    def get_success_url(self):
        return reverse('recipe-detail', kwargs={'pk': self.object.recipe.id})


class RecipeToolCreateView(LoginRequiredMixin, CreateView):
    model = recipe_tool
    form_class = CreateTool

    # template_name = 'index_home/recipe_tool_form.html'

    def form_valid(self, form):
        # form.instance.recipe = self.request.recipe.name
        messages.success(self.request, f'Successfully Added!')
        return super().form_valid(form)

    def get_absolute_url(self):
        return u'/recipe/%d' % self.id


class RecipeToolUpdateView(LoginRequiredMixin, UpdateView):
    model = recipe_tool
    form_class = CreateTool

    def form_valid(self, form):
        messages.success(self.request, f'Successfully Updated!')
        return super().form_valid(form)


class RecipeToolDeleteView(LoginRequiredMixin, DeleteView):
    model = recipe_tool
    form_class = CreateTool

    def get_success_url(self):
        return reverse('recipe-detail', kwargs={'pk': self.object.recipe.id})


class ScheduleDetailView(ListView):
    model = recipe_scheduling
    context_object_name = 'schedules'

    def get_queryset(self):
        return self.model.objects.all()


class ScheduleCreateView(LoginRequiredMixin, CreateView):
    model = recipe_scheduling
    form_class = CreateSchedule

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, f'Successfully Added!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ScheduleCreateView, self).get_context_data(**kwargs)
        return context


class ScheduleUpdateView(LoginRequiredMixin, UpdateView):
    model = recipe_scheduling
    form_class = CreateSchedule

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, f'Successfully Updated!')
        return super().form_valid(form)


class ScheduleDeleteView(LoginRequiredMixin, DeleteView):
    model = recipe_scheduling
    form_class = CreateSchedule

    def get_success_url(self):
        return reverse('recipe-scheduling', kwargs={'username': self.request.user})


def LikeView(request, pk):
    recipe = get_object_or_404(Recipe, id=request.POST.get('post_id'))
    liked = False
    if recipe.hearts.filter(id=request.user.id).exists():
        recipe.hearts.remove(request.user)
        liked = False
    else:
        recipe.hearts.add(request.user)
        liked = True
    return redirect(reverse('recipe-detail', args={str(pk)}))


class RecipeIngres2CreateView(LoginRequiredMixin, CreateView):
    model = ReceIngres2
    form_class = CreateIngredient2

    def form_valid(self, form):
        messages.success(self.request, f'Successfully Added!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(RecipeIngres2CreateView, self).get_context_data(**kwargs)
        return context


class RecipeIngres2UpdateView(LoginRequiredMixin, UpdateView):
    model = ReceIngres2
    form_class = CreateIngredient2

    def form_valid(self, form):
        messages.success(self.request, f'Successfully Updated!')
        return super().form_valid(form)


class RecipeIngres2DeleteView(LoginRequiredMixin, DeleteView):
    model = ReceIngres2
    form_class = CreateIngredient2

    def get_success_url(self):
        return reverse('recipe-detail', kwargs={'pk': self.object.recipe.id})


class TablesToBeDownloaded(ListView):
    model = Recipe
    template_name = 'index_home/tables.html'

    def get_context_data(self, **kwargs):
        context = super(TablesToBeDownloaded, self).get_context_data(**kwargs)
        context['Recipes'] = Recipe.objects.all()
        context['Ingres'] = ReceIngres.objects.all()
        context['Steps'] = Step.objects.all()
        context['Users'] = User.objects.all()
        return context


class UserLogs(ListView):
    model = Logs_recipes
    template_name = 'index_home/admin_logs.html'

    def get_context_data(self, **kwargs):
        context = super(UserLogs, self).get_context_data(**kwargs)
        context['Total_Recipe'] = No_Recipe.objects.first()
        context['Total_Users'] = No_Users.objects.first()
        context['Total_Categories'] = No_Categories.objects.first()
        context['Total_Ingres'] = No_Ingres.objects.first()
        context['Total_Skills'] = No_Skills.objects.first()
        context['Total_Tools'] = No_Tools.objects.first()
        context['Total_Tags'] = No_Tags.objects.first()
        context['Total_Units'] = No_Units.objects.first()
        context['Users'] = User.objects.all()
        context['Logs'] = Logs_recipes.objects.all()
        return context
