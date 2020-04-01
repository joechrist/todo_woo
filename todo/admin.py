from django.contrib import admin
from .models import Todo

# Custum admin file and created field to readonly


class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


admin.site.register(Todo, TodoAdmin)
