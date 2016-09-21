from django.test import TestCase
from books.models import Book, Category


def create_test_book(name, category):
    return Book.objects.create(name=name, category=category)


class TestBookView(TestCase):
    def setUp(self):
        self.test_category = Category.objects.create(name='Fiction')

    def test_view_with_no_books(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['boks']), 0)

    def test_view_with_created_book(self):
        fiction_book = create_test_book(
            name='Harry Potter', category=self.test_category)
        response = self.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['books']), 1)
        self.assertEqual(response.context['books'][0], fiction_book)

    def test_can_search_by_book_name(self):
        fiction_book = create_test_book(
            name='Harry Potter', category=self.test_category)
        response = self.client.get('/?name=harry')
        self.assertEqual(response.context['books'], 1)
        result = response.context['books'][0]
        self.assertEqual(result.name, fiction_book.name)

    def test_can_search_by_category(self):
        fiction_book = create_test_book(
            name='Lord of the Rings', category=self.test_category)
        response = self.client.get('/?name=&category=fiction')
        result = response.context['books'][0]
        self.assertEqual(result.category, fiction_book.category)
