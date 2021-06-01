from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import RecipeListView, RecipeDetailView, RecipeCreateView, RecipeUpdateView, RecipeDeleteView, \
    UserRecipeListView, RecipeListViewBase, \
    RecipeIngredientView, UsersListView, \
    SkillCreateView, SkillUpdateView, SkillDeleteView, \
    RecipeToolCreateView, RecipeToolUpdateView, RecipeToolDeleteView, \
    AdminCategoriesListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView, \
    AdminIngredientListView, IngredientCreateView, IngredientUpdateView, IngredientDeleteView, \
    AdminSkillsListView, SkillsCreateView, SkillsUpdateView, SkillsDeleteView, \
    AdminToolsListView, ToolsCreateView, ToolsUpdateView, ToolsDeleteView, \
    AdminTagsListView, TagsCreateView, TagsUpdateView, TagsDeleteView, \
    AdminUnitsListView, UnitCreateView, UnitUpdateView, UnitDeleteView, \
    AdminRecipeListView, RecipesCreateView, RecipesUpdateView, RecipesDeleteView, \
    RecipeIngresCreateView, RecipeIngresUpdateView, RecipeIngresDeleteView, \
    PreparationCreateView, PreparationUpdateView, PreparationDeleteView, \
    ScheduleDetailView, ScheduleCreateView, ScheduleUpdateView, ScheduleDeleteView, \
    RecipeIngres2CreateView, RecipeIngres2UpdateView, RecipeIngres2DeleteView, TablesToBeDownloaded, \
    UserLogs
from .models import Recipe

urlpatterns = [
    path('', views.home, name='index-home'),
    path('user/<str:username>', UserRecipeListView.as_view(), name='user-recipe'),
    path('recipe/new/', RecipeCreateView.as_view(), name='recipe-create'),
    path('recipe/<int:pk>/update/', RecipeUpdateView.as_view(), name='recipe-update'),
    path('recipe/<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe-delete'),
    path('packages/', views.packages, name='index-packages'),
    path('help/', views.help, name='index-help'),
    path('recipes/', RecipeListView.as_view(), name='index-blog'),
    path('heart/<int:pk>/', views.LikeView, name='like-recipe'),
    path('contact/', views.contact, name='index-contact'),
    path('search/', views.add, name='add'),
    # path('search/', views.search, name='search'),
    path('basket/', views.basket, name='basket'),
    path('unit/', views.unit_converter, name='unit'),
    path('create/', views.hotel_image_view, name='create'),
    path('success/', views.success, name='success'),
    path('admins/home/', views.admin_home, name='admin-home'),
    path('admins/users/', UsersListView.as_view(), name='admin-users'),
    path('admins/categories/', AdminCategoriesListView.as_view(), name='admin-categories'),
    path('admins/categories/new/', CategoryCreateView.as_view(), name='new-categories'),
    path('admins/categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='update-categories'),
    path('admins/categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='delete-categories'),
    path('admins/ingredients/', AdminIngredientListView.as_view(), name='admin-ingredients'),
    path('admins/ingredients/new/', IngredientCreateView.as_view(), name='new-ingredients'),
    path('admins/ingredients/<int:pk>/update/', IngredientUpdateView.as_view(), name='update-ingredients'),
    path('admins/ingredients/<int:pk>/delete/', IngredientDeleteView.as_view(), name='delete-ingredients'),
    path('admins/skills/', AdminSkillsListView.as_view(), name='admin-skills'),
    path('admins/skills/new/', SkillsCreateView.as_view(), name='new-skills'),
    path('admins/skills/<int:pk>/update/', SkillsUpdateView.as_view(), name='update-skills'),
    path('admins/skills/<int:pk>/delete/', SkillsDeleteView.as_view(), name='delete-skills'),
    path('admins/tools/', AdminToolsListView.as_view(), name='admin-tools'),
    path('admins/tools/new/', ToolsCreateView.as_view(), name='new-tools'),
    path('admins/tools/<int:pk>/update/', ToolsUpdateView.as_view(), name='update-tools'),
    path('admins/tools/<int:pk>/delete/', ToolsDeleteView.as_view(), name='delete-tools'),
    path('admins/tags/', AdminTagsListView.as_view(), name='admin-tags'),
    path('admins/tags/new/', TagsCreateView.as_view(), name='new-tags'),
    path('admins/tags/<int:pk>/update/', TagsUpdateView.as_view(), name='update-tags'),
    path('admins/tags/<int:pk>/delete/', TagsDeleteView.as_view(), name='delete-tags'),
    path('admins/units/', AdminUnitsListView.as_view(), name='admin-units'),
    path('admins/units/new/', UnitCreateView.as_view(), name='new-units'),
    path('admins/units/<int:pk>/update/', UnitUpdateView.as_view(), name='update-units'),
    path('admins/units/<int:pk>/delete/', UnitDeleteView.as_view(), name='delete-units'),
    path('admins/recipes/', AdminRecipeListView.as_view(), name='admin-recipes'),
    path('admins/recipes/new/', RecipesCreateView.as_view(), name='new-recipes'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('admins/recipes/<int:pk>/update/', RecipesUpdateView.as_view(), name='update-recipes'),
    path('admins/recipes/<int:pk>/delete/', RecipesDeleteView.as_view(), name='delete-recipes'),
    path('recipe/ingre/<int:pk>/', RecipeIngresCreateView.as_view(), name='add-ingredient'),
    path('recipe/ingre/<int:pk>/update/', RecipeIngresUpdateView.as_view(), name='update-ingre'),
    path('recipe/ingre/<int:pk>/delete/', RecipeIngresDeleteView.as_view(), name='delete-ingre'),
    path('recipe/preparation/<int:pk>/', PreparationCreateView.as_view(), name='add-preparation'),
    path('recipe/preparation/<int:pk>/update/', PreparationUpdateView.as_view(), name='update-preparation'),
    path('recipe/preparation/<int:pk>/delete/', PreparationDeleteView.as_view(), name='delete-preparation'),
    path('recipe/skill/<int:pk>/', SkillCreateView.as_view(), name='add-recipe-skill'),
    path('recipe/skill/<int:pk>/update/', SkillUpdateView.as_view(), name='update-skill'),
    path('recipe/skill/<int:pk>/delete/', SkillDeleteView.as_view(), name='delete-skill'),
    path('recipe/tool/', RecipeToolCreateView.as_view(), name='add-recipe-tool'),
    path('recipe/tool/<int:pk>/update/', RecipeToolUpdateView.as_view(), name='update-tool'),
    path('recipe/tool/<int:pk>/delete/', RecipeToolDeleteView.as_view(), name='delete-tool'),
    path('recipe/schedule/<str:username>/', ScheduleDetailView.as_view(), name='recipe-scheduling'),
    path('recipe/schedule/<str:username>/new/', ScheduleCreateView.as_view(), name='add-scheduling'),
    path('recipe/schedule/<int:pk>/update/', ScheduleUpdateView.as_view(), name='update-scheduling'),
    path('recipe/schedule/<int:pk>/delete/', ScheduleDeleteView.as_view(), name='delete-scheduling'),
    path('recipe/ingre2/<int:pk>/new', RecipeIngres2CreateView.as_view(), name='add-ingredients2'),
    path('recipe/ingre2/<int:pk>/update/', RecipeIngres2UpdateView.as_view(), name='update-ingredients2'),
    path('recipe/ingre2/<int:pk>/delete/', RecipeIngres2DeleteView.as_view(), name='delete-ingredients2'),
    path('tables', TablesToBeDownloaded.as_view(), name='tables'),
    path('admins/userlogs', UserLogs.as_view(), name='user-logs'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
