from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'', views.BookListView, name='book_list'),
]
