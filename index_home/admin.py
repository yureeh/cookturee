from django.contrib import admin
from .models import Recipe, Heart, Statistics, Ingredients, Tags, Ingretype, Category, Unit, ReceIngres, \
    Tag_id, UnitRatio, Post, Hotel, Unit_type, Step, Skill, Tool, recipe_tool, recipe_skill, \
    recipe_scheduling, ReceIngres2, TempRecipes, TempCategories, TempSkills, TempTools

admin.site.register(Recipe)
admin.site.register(Ingredients)
admin.site.register(Tags)
admin.site.register(Category)
admin.site.register(Unit)
admin.site.register(ReceIngres)
admin.site.register(Skill)
admin.site.register(Tool)
admin.site.register(recipe_skill)
admin.site.register(recipe_scheduling)
admin.site.register(TempRecipes)
admin.site.register(TempCategories)
admin.site.register(TempSkills)
admin.site.register(TempTools)
