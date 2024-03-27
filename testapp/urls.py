from django.urls import path
from .views import BookDetailView

urlpatterns = [
    path('book/<int:pk>', BookDetailView.as_view(), name='book-detail'),
]