from django_filters import rest_framework as filters
from api.models import Classe


class ClasseFilter(filters.FilterSet):
    class Meta:
        model = Classe
        fields = ('nom', 'prix', 'matiere', 'niveau')
