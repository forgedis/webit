from django.contrib import admin

from todo.models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'completed', 'created_at', 'updated_at']
    list_filter = ['completed']
    search_fields = ['title', 'description']