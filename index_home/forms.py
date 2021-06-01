from django import forms
from .models import Recipe, Hotel, ReceIngres, Step, recipe_skill, recipe_tool, Category, Ingredients, Skill, Tool, \
    Tags, Unit, recipe_scheduling, ReceIngres2

DISPLAY_CHOICES = (
    ("locationbox", "Display Location"),
    ("displaybox", "Display Direction")
)


class MyForm(forms.Form):
    something_truthy = forms.BooleanField(required=False)


class RecipePhotoUpdateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['photo']


class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['name', 'hotel_Main_Img']


class CreateRecipe(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ['name', 'description', 'chef_tips', 'service_size', 'preparation_time', 'cooking_time',
                  'categories', 'tags', 'Source_URL']

    def __init__(self, *args, **kwargs):
        super(CreateRecipe, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['chef_tips'].widget.attrs['class'] = 'form-control'
        self.fields['service_size'].widget.attrs['class'] = 'form-control'
        self.fields['preparation_time'].widget.attrs['class'] = 'form-control'
        self.fields['cooking_time'].widget.attrs['class'] = 'form-control'
        self.fields['Source_URL'].widget.attrs['class'] = 'form-control'
        self.fields['categories'].widget.attrs['class'] = 'form-control'
        self.fields['tags'].widget.attrs['class'] = 'form-control'

        self.fields['name'].widget.attrs['placeholder'] = 'Enter recipe name'
        self.fields['description'].widget.attrs['placeholder'] = 'Describe your recipe'
        self.fields['chef_tips'].widget.attrs['placeholder'] = 'Enter tips for your recipe'
        self.fields['service_size'].widget.attrs['placeholder'] = 'Enter the service size'
        self.fields['preparation_time'].widget.attrs['placeholder'] = 'How long does it takes to prepare your recipe?'
        self.fields['cooking_time'].widget.attrs['placeholder'] = 'How long does it takes to cook your recipe?'
        self.fields['Source_URL'].widget.attrs['placeholder'] = 'paste url if this recipe is from other website'


class CreateRecipe2(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ['name', 'privacy', 'description', 'chef_tips', 'service_size', 'preparation_time',
                  'cooking_time', 'categories', 'tags', 'Source_URL']

    def __init__(self, *args, **kwargs):
        super(CreateRecipe2, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['chef_tips'].widget.attrs['class'] = 'form-control'
        self.fields['service_size'].widget.attrs['class'] = 'form-control'
        self.fields['preparation_time'].widget.attrs['class'] = 'form-control'
        self.fields['cooking_time'].widget.attrs['class'] = 'form-control'
        self.fields['Source_URL'].widget.attrs['class'] = 'form-control'
        self.fields['privacy'].widget.attrs['class'] = 'form-control'
        self.fields['categories'].widget.attrs['class'] = 'form-control'
        self.fields['tags'].widget.attrs['class'] = 'form-control'

        self.fields['name'].widget.attrs['placeholder'] = 'Enter recipe name'
        self.fields['description'].widget.attrs['placeholder'] = 'Describe your recipe'
        self.fields['chef_tips'].widget.attrs['placeholder'] = 'Enter tips for your recipe'
        self.fields['service_size'].widget.attrs['placeholder'] = 'Enter the service size'
        self.fields['preparation_time'].widget.attrs['placeholder'] = 'How long does it takes to prepare your recipe?'
        self.fields['cooking_time'].widget.attrs['placeholder'] = 'How long does it takes to cook your recipe?'
        self.fields['Source_URL'].widget.attrs['placeholder'] = 'paste url if this recipe is from other website'


class CreateIngredient(forms.ModelForm):
    class Meta:
        model = ReceIngres
        fields = ['quantity', 'unit', 'ingredient', 'other']

    def __init__(self, *args, **kwargs):
        super(CreateIngredient, self).__init__(*args, **kwargs)
        self.fields['quantity'].widget.attrs['class'] = 'form-control'
        self.fields['unit'].widget.attrs['class'] = 'form-control'
        self.fields['ingredient'].widget.attrs['class'] = 'form-control'
        self.fields['other'].widget.attrs['class'] = 'form-control'
        # self.fields['recipe'].widget.attrs['class'] = 'form-control'


class CreateIngredient2(forms.ModelForm):
    class Meta:
        model = ReceIngres
        fields = ['quantity', 'unit', 'ingredient', 'other']

    def __init__(self, *args, **kwargs):
        super(CreateIngredient2, self).__init__(*args, **kwargs)
        self.fields['quantity'].widget.attrs['class'] = 'form-control'
        self.fields['unit'].widget.attrs['class'] = 'form-control'
        self.fields['ingredient'].widget.attrs['class'] = 'form-control'
        self.fields['other'].widget.attrs['class'] = 'form-control'


class CreatePreparation(forms.ModelForm):
    class Meta:
        model = Step
        fields = ['order', 'step']

    def __init__(self, *args, **kwargs):
        super(CreatePreparation, self).__init__(*args, **kwargs)
        self.fields['order'].widget.attrs['class'] = 'form-control'
        self.fields['step'].widget.attrs['class'] = 'form-control'
        # self.fields['recipe'].widget.attrs['class'] = 'form-control'


class CreateSkill(forms.ModelForm):
    class Meta:
        model = recipe_skill
        fields = ['recipe', 'skill']

    def __init__(self, *args, **kwargs):
        super(CreateSkill, self).__init__(*args, **kwargs)
        self.fields['skill'].widget.attrs['class'] = 'form-control'
        self.fields['recipe'].widget.attrs['class'] = 'form-control'


class CreateTool(forms.ModelForm):
    class Meta:
        model = recipe_tool
        fields = ['tool', 'recipe']

    def __init__(self, *args, **kwargs):
        super(CreateTool, self).__init__(*args, **kwargs)
        self.fields['tool'].widget.attrs['class'] = 'form-control'
        self.fields['recipe'].widget.attrs['class'] = 'form-control'


class CreateCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category']

    def __init__(self, *args, **kwargs):
        super(CreateCategory, self).__init__(*args, **kwargs)
        self.fields['category'].widget.attrs['class'] = 'form-control'


class CreateIngredients(forms.ModelForm):
    class Meta:
        model = Ingredients
        fields = ['name', 'type']

    def __init__(self, *args, **kwargs):
        super(CreateIngredients, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['type'].widget.attrs['class'] = 'form-control'


class CreateSkills(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['skill']

    def __init__(self, *args, **kwargs):
        super(CreateSkills, self).__init__(*args, **kwargs)
        self.fields['skill'].widget.attrs['class'] = 'form-control'


class CreateTools(forms.ModelForm):
    class Meta:
        model = Tool
        fields = ['tool']

    def __init__(self, *args, **kwargs):
        super(CreateTools, self).__init__(*args, **kwargs)
        self.fields['tool'].widget.attrs['class'] = 'form-control'


class CreateTags(forms.ModelForm):
    class Meta:
        model = Tags
        fields = ['tag']

    def __init__(self, *args, **kwargs):
        super(CreateTags, self).__init__(*args, **kwargs)
        self.fields['tag'].widget.attrs['class'] = 'form-control'


class CreateUnits(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['unit', 'abb', 'type']

    def __init__(self, *args, **kwargs):
        super(CreateUnits, self).__init__(*args, **kwargs)
        self.fields['unit'].widget.attrs['class'] = 'form-control'
        self.fields['abb'].widget.attrs['class'] = 'form-control'
        self.fields['type'].widget.attrs['class'] = 'form-control'


class CreateSchedule(forms.ModelForm):
    class Meta:
        model = recipe_scheduling
        fields = ['recipe', 'alarm', 'note']

    def __init__(self, *args, **kwargs):
        super(CreateSchedule, self).__init__(*args, **kwargs)
        self.fields['recipe'].widget.attrs['class'] = 'form-control'
        self.fields['alarm'].widget.attrs['class'] = 'form-control'
        self.fields['note'].widget.attrs['class'] = 'form-control'


