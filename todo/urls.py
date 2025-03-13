from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet, TodoListView, TodoCreateView

router = DefaultRouter()
router.register(r'todos', TodoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', TodoListView.as_view(), name='todo-list'),
    path('create/', TodoCreateView.as_view(), name='todo-create'),

]
