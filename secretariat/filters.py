import django_filters
from .models import LogisticsRequest
from delegation.models import Delegate, Allocation


class RequestFilter(django_filters.FilterSet):
    class Meta:
        model = LogisticsRequest
        fields = {'committee': ['exact', ],
                  'description': ['icontains', ],
                  'completed': ['exact', ],
                  }


class DelegateFilter(django_filters.FilterSet):
    class Meta:
        model = Delegate
        fields = {
            'delegation': ['exact', ],
            'committee_preference': ['exact', ],
            'country_preference': ['exact', ],
        }


class AllocationFilter(django_filters.FilterSet):
    class Meta:
        model = Allocation
        fields = {
            'committee': ['exact', ],
        }
