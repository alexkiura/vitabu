from django.views.generic.list import ListView # pragma: no cover
from .models import Book, Category # pragma: no cover


class BookListView(ListView):
    template_name = 'books/book_list.html'
    model = Book

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['books'] = self.get_queryset()
        return context

    def get_queryset(self):
        name_query = self.request.GET.get('name')
        category_query = self.request.GET.get('category')
        if category_query:
            category = Category.objects.filter(
                name__icontains=category_query).first()
            if name_query:
                return Book.objects.filter(
                    name__icontains=name_query, category=category)
            return Book.objects.filter(category=category)
        if name_query:
            return Book.objects.filter(name__icontains=name_query)
        return Book.objects.all()
