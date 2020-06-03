from django.urls import path, include
from rest_framework.routers import DefaultRouter

from todos import views


router = DefaultRouter()
router.register('todos', views.TodoViewSet)

app_name = 'todos'

urlpatterns = [
    path('', include(router.urls))
]
