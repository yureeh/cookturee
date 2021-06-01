import django_filters
from .models import Recipe


class RecipesFilter(django_filters.FilterSet):
    CHOICES = (
        ('ascending', 'Ascending'),
        ('descending', 'Descending'),
    )
    ordering = django_filters.ChoiceFilter(label="Ordering", choices=CHOICES, method='filter_by_ordering')

    class Meta:
        model = Recipe
        fields = {
            'name': ['icontains'],
            'description': ['icontains']
        }

    def filter_by_ordering(self, queryset, name, value):
        expression = 'name' if value == 'ascending' else '-name'
        return queryset.order_by(expression)