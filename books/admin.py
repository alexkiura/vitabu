from django.contrib import admin # pragma: no cover
from .models import Book, Category # pragma: no cover

admin.site.register(Book)
admin.site.register(Category)
