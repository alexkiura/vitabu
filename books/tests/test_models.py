from django.test import TestCase
from books.models import Book, Category

class TestModels(TestCase):

    def setUp(self):
        self.test_category = Category.objects.create(name='General')
        self.test_book = Book.objects.create(
            name='Life', category=self.test_category)

    def test_can_create_categories(self):
        fiction_category = Category.objects.create(name='Fiction')
        created_category = Category.objects.filter(name='Fiction').first()
        self.assertEqual(fiction_category, created_category)
        self.assertEqual(len(Category.objects.all()), 2)

    def test_can_create_books(self):
        general_book = Book.objects.create(
            name='General book', category=self.test_category)
        created_book = Book.objects.filter(name='General book').first()
        self.assertEqual(general_book, created_book)
        self.assertEqual(len(Book.objects.all()), 2)

    def test_can_edit_books(self):
        life_book = Book.objects.filter(name='Life').first()
        life_book.name = 'Wiki'
        life_book.save()
        self.assertEqual(life_book.name, 'Wiki')
