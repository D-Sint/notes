from django.contrib import admin

from notes.models import Category, Note

admin.site.register(Note)
admin.site.register(Category)

