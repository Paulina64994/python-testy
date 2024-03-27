from django.test import TestCase
from django.urls import reverse
from testapp.models import Book
from datetime import datetime, timedelta
# Create your tests here.

class BookModelTest(TestCase):

    def setUp(self):
        Book.objects.create(title="Test Book", author="Author Name", borrow_count=101,
                            published_date=datetime.now().date() - timedelta(days=30))
        Book.objects.create(title="Another Test Book", author="Another Author", borrow_count=50,
                            published_date=datetime.now().date() - timedelta(days=800))

    def test_is_popular(self):
        popular_book = Book.objects.get(title="Test Book")
        not_popular_book=Book.objects.get(title="Another Test Book")

        self.assertTrue(popular_book.is_popular())
        self.assertFalse(not_popular_book.is_popular())

