from django.test import TestCase
from django.urls import reverse
from testapp.models import Book, ListBike
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

    def test_book_creation(self):
        book = Book.objects.get(title="Test Book")

        self.assertEqual(book.author, "Author Name")
        self.assertEqual(book.borrow_count, 101)

    def test_genre(self):
        book = Book.objects.get(title="Test Book")
        book.genre = "Fantasy"
        book.save()
        self.assertEqual(book.genre, "Fantasy")

    def test_string_representation(self):
     book = Book.objects.get(title="Test Book")
     self.assertEqual(book.string_representation(), "Test Book by Author Name")

    def test_get_absolute_url(self):
        book = Book.objects.get(title="Test Book")
        self.assertEqual(book.get_absolute_url(), reverse('book-detail', kwargs={'pk': book.pk}))

    def test_available_default(self):
        book = Book.objects.get(title="Test Book")
        self.assertTrue(book.available)

    def test_reserve_method(self):
        book = Book.objects.get(title="Test Book")
        book.reserve()
        self.assertFalse(book.available)

    def test_is_new_release(self):
        new_release_book = Book.objects.get(title="Test Book")
        self.assertTrue(new_release_book.is_new_release())
        not_new_release_book = Book

class BikeModelTest(TestCase):

    def setUp(self):
        ListBike.objects.create(nameBike="Test Bike", content="Space text", price=1003,
                            year=2000)
        ListBike.objects.create(nameBike="Another Test Bike", content="Space text", price=50,
                            year = 2022)

    def test_is_expensive(self):
        expensive_bike = ListBike.objects.get(nameBike="Test Bike")
        cheap_bike = ListBike.objects.get(nameBike="Another Test Bike")

        self.assertTrue(expensive_bike.is_expesive())
        self.assertFalse(cheap_bike.is_expesive())

    def test_bike_creation(self):
        bike = ListBike.objects.get(nameBike="Test Bike")

        self.assertEqual(bike.content, "Space text")
        self.assertEqual(bike.price, 1003)
    def test_genre(self):
        bike = ListBike.objects.get(nameBike="Test Bike")
        bike.price = 1030
        bike.save()
        self.assertEqual(bike.price, 1030)

    def test_string_representation(self):
     bike = ListBike.objects.get(nameBike="Test Bike")
     self.assertEqual(bike.string_representation(), "Test Bike from 2000")

