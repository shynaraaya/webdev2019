from django_filters import rest_framework as filters
from .models import Task

class TaskFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')
    min_id = filters.NumberFilter(field_name='id', lookup_expr='gte')
    max_id = filters.NumberFilter(field_name='id', lookup_expr='lte')


    class Meta:
        model = Task
        fields = ('name', 'id')