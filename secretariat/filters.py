import django_filters
from .models import LogisticsRequest

class RequestFilter(django_filters.FilterSet):
    class Meta:
        model = LogisticsRequest
        fields = {'committee': ['exact',],
                  'description': ['icontains',],
                  'completed': ['exact',],
                  }
