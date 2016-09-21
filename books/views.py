from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Book, Category


class BookListView(ListView):
    template_name = 'books/book_list.html'
    model = Book

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['books'] = self.get_queryset()
        return context

    def get_queryset(self):
        return Book.objects.all()
