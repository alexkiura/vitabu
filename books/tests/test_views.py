from django.test import TestCase
from books.models import Book, Category




class TestBookView(TestCase):
    def setUp(self):
        self.test_category = Category.objects.create(name='Fiction')

    def test_view_with_no_books(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['books']), 0)

    def test_view_with_created_book(self):
        fiction_book = Book.objects.create(
            name='Harry Potter', category=self.test_category)
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['books']), 1)
        self.assertEqual(response.context['books'][0], fiction_book)

    def test_can_search_by_book_name(self):
        fiction_book = Book.objects.create(
            name='Harry Potter', category=self.test_category)
        response = self.client.get('/?name=harry')
        self.assertEqual(len(response.context['books']), 1)
        result = response.context['books'][0]
        self.assertEqual(result.name, fiction_book.name)

    def test_can_search_by_category(self):
        fiction_book = Book.objects.create(
            name='Lord of the Rings', category=self.test_category)
        response = self.client.get('/?name=&category=fiction')
        result = response.context['books'][0]
        self.assertEqual(result.category, fiction_book.category)

    def test_searching_books_that_dont_exist(self):
        response = self.client.get('/?name=&category=lokop')
        self.assertEqual(len(response.context['books']), 0)
        self.assertIn('No such book exists', response.content)
