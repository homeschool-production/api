from rest_framework.routers import DefaultRouter
from .views import ChapitreClasseListView, ChapitreClasseViewSet
from django.urls import path, include


urlpatterns = [
    path('list/', ChapitreClasseListView.as_view(), name='chapitre-list')
]

router = DefaultRouter()
router.register('', ChapitreClasseViewSet, basename='chapitre')

urlpatterns += router.urls