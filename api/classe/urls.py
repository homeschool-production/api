from rest_framework.routers import DefaultRouter
from .views import ClasseViewSet, ClasseListView, ClasseListFilteredView
from django.urls import path, include
from api.models import Eleve

urlpatterns = [
    path('list/', ClasseListView.as_view(), name='classe-list'),
    path('list_filtered/', ClasseListFilteredView.as_view(), name='classe-list-filtered')
]

router = DefaultRouter()
router.register('', ClasseViewSet, basename='classe')

urlpatterns += router.urls