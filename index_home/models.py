from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

PRIVACY_CHOICES = (
    ('PUBLIC', 'Public'),
    ('PRIVATE', 'Private'),
)


class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse('admin-categories')


class Tags(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('admin-tags')


class Tool(models.Model):
    tool = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.tool

    def get_absolute_url(self):
        return reverse('admin-tools')


class Skill(models.Model):
    skill = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.skill

    def get_absolute_url(self):
        return reverse('admin-skills')


class Ingretype(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class Ingredients(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(Ingretype, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('admin-ingredients')


class Unit_type(models.Model):
    type = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.type


class Unit(models.Model):
    unit = models.CharField(max_length=100, null=True)
    abb = models.CharField(max_length=100, null=True)
    type = models.ForeignKey(Unit_type, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.unit

    def get_absolute_url(self):
        return reverse('admin-units')


class ReceIngres2(models.Model):
    quantity = models.CharField(max_length=50)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    other = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return "{} {} {}".format(self.quantity, self.unit, self.ingredient)

    def get_absolute_url(self):
        return reverse('recipe-detail', kwargs={'pk': self.recipe.id})


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(default='default_recipe.jpg', upload_to='recipe_img', null=True)
    privacy = models.CharField(max_length=10, choices=PRIVACY_CHOICES)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    chef_tips = models.TextField(blank=True)
    service_size = models.IntegerField(null=True)
    preparation_time = models.TimeField(null=True)
    cooking_time = models.TimeField(null=True)
    Source_URL = models.TextField(blank=True)
    hearts = models.ManyToManyField(User, related_name="likes")
    ingredients = models.ManyToManyField(ReceIngres2, related_name="ingredients")
    categories = models.ManyToManyField(Category, related_name="categories", null=True, blank=True)
    tags = models.ManyToManyField(Tags, related_name="tags", null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)

    def total_hearts(self):
        return self.hearts.count()

    def get_absolute_url(self):
        return reverse('recipe-detail', kwargs={'pk': self.pk})


class Heart(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    heart = models.BooleanField()
    viewed = models.BooleanField()

    def __str__(self):
        return "{} : {} : {} {}".format(self.recipe_id, self.user_id, self.heart, self.viewed)


class Statistics(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    total_heart = models.IntegerField()
    total_views = models.IntegerField(null=True)
    average = models.FloatField()
    score = models.FloatField()


# class hybrid(models.Model):
#     raw_key = models.CharField(max_length=255, blank=True)
#
#     def __str__(self):
#         return self.raw_key


class checked_insert(models.Model):
    coursename = models.CharField(max_length=100)


class ReceIngres(models.Model):
    quantity = models.CharField(max_length=50)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    ingredient = models.CharField(max_length=250)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    other = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return "{} {} {} {}".format(self.quantity, self.unit, self.ingredient, self.recipe)

    def get_absolute_url(self):
        return reverse('recipe-detail', kwargs={'pk': self.recipe.id})


class Tag_id(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)

    def __str__(self):
        return self.recipe.name

    def get_absolute_url(self):
        return reverse('recipe-detail', kwargs={'pk': self.recipe.id})


class UnitRatio(models.Model):
    unitA = models.ForeignKey(Unit, related_name='UnitA', null=True, on_delete=models.CASCADE)
    unitB = models.ForeignKey(Unit, related_name='UnitB', null=True, on_delete=models.CASCADE)
    one = models.IntegerField()
    result = models.FloatField()

    def __str__(self):
        return "{} {} : {} {}".format(self.one, self.unitA, self.result, self.unitB)


class Post(models.Model):
    title = models.CharField(max_length=300, unique=True)
    content = models.TextField()


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    hotel_Main_Img = models.ImageField(upload_to='images/')


class Step(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    order = models.IntegerField(null=True)
    step = models.TextField()

    def __str__(self):
        return self.step

    def get_absolute_url(self):
        return reverse('recipe-detail', kwargs={'pk': self.recipe.id})


class recipe_tool(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)

    def __str__(self):
        return self.tool.tool

    def get_absolute_url(self):
        return reverse('recipe-detail', kwargs={'pk': self.recipe.id})


class recipe_skill(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.skill.skill

    def get_absolute_url(self):
        return reverse('recipe-detail', kwargs={'pk': self.recipe.id})


class recipe_scheduling(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    alarm = models.DateTimeField()
    note = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):  # 'recipe-scheduling' user.username
        return reverse('recipe-scheduling', kwargs={'username': self.user.username})


class TempRecipes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "temp_recipes"


class TempCategories(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    categories = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "recipe_categories_info"


class TempTools(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    tools = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "recipe_tools_info"


class TempSkills(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    skills = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "recipe_skills_info"


class TempHearts(models.Model):
    id = models.IntegerField(primary_key=True)
    total_hearts = models.IntegerField()

    class Meta:
        managed = False
        ordering = ('-total_hearts',)
        db_table = "recipe_hearts_info"


class User_Recipe(models.Model):
    author_id = models.IntegerField(primary_key=True)
    No_of_Recipes = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "user_recipes"


class No_Recipe(models.Model):
    No_of_Recipes = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = "count_recipes"


class No_Users(models.Model):
    total = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = "no_users"


class No_Categories(models.Model):
    total = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = "no_categories"


class No_Ingres(models.Model):
    total = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = "no_ingres"


class No_Skills(models.Model):
    total = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = "no_skill"


class No_Tools(models.Model):
    total = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = "no_tools"


class No_Tags(models.Model):
    total = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = "no_tags"


class No_Units(models.Model):
    total = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = "no_units"


class No_Submitted(models.Model):
    total = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = "submitted_recipes"


class No_Featured(models.Model):
    id = models.IntegerField(primary_key=True)
    total_hearts = models.IntegerField()
    name = models.TextField(blank=True)
    username = models.TextField(blank=True)
    date_added = models.TextField(blank=True)
    description = models.TextField(blank=True)
    ingredients = models.TextField(blank=True)
    privacy = models.TextField(blank=True)
    chef_tips = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = "new_info"


class Logs_recipes(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.IntegerField(blank=True)
    acts = models.TextField(blank=True)
    date_logs = models.DateTimeField(default=timezone.now)


class Concat_Recipe_info(models.Model):
    id = models.IntegerField(primary_key=True)
    mass_info = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = "concat_recipe_info"

class sample_table(models.Model):
    name = models.TextField()
    age = models.IntegerField()
    descp = models.TextField()
    total = models.TextField()