from rest_framework.routers import DefaultRouter
from .views import ClasseViewSet, ClasseListView
from django.urls import path, include
from api.models import Eleve

urlpatterns = [
    path('list/', ClasseListView.as_view(), name='classe-list')
]

router = DefaultRouter()
router.register('', ClasseViewSet, basename='classe')

urlpatterns += router.urls