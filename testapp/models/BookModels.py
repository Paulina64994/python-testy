from django.db import models
from django.urls import reverse
from datetime import datetime, timedelta
from datetime import date

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, blank=True)
    borrow_count = models.IntegerField(default=0)
    published_date = models.DateField(default=date.today)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def is_popular(self):
        return self.borrow_count > 100

    def is_new_release(self):
        return (datetime.now().date() - self.published_date) <= timedelta(days=730)

    def string_representation(self):
        return f"{self.title} by {self.author}"

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk': self.pk})

    def reserve(self):
        self.available = False
        self.save()

