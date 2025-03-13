from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from rest_framework.viewsets import ModelViewSet

from todo.models import Todo
from todo.serializer import TodoSerializer


class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoListView(ListView):
    model = Todo
    template_name = 'todo/todo_list.html'
    context_object_name = 'todos'
    ordering = ['-created_at']


class TodoCreateView(CreateView):
    model = Todo
    template_name = 'todo/todo_form.html'
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('todo-list')  # 🔥 Ensure this name matches your URLs
