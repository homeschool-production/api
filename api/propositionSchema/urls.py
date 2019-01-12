from rest_framework.routers import DefaultRouter
from .views import QuestionListView, QuestionViewSet
from django.urls import path, include


urlpatterns = [
    path('list/', QuestionListView.as_view(), name='question-list')
]

router = DefaultRouter()
router.register('', QuestionViewSet, basename='question')

urlpatterns += router.urls