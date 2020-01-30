from django.db import models
from datetime import datetime
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Author(models.Model):
    authorName = models.CharField(max_length=100)

    # get author url by id
    def get_author_url(self):
        return reverse('author_detail_view', kwargs={'id': self.id})

class Book(models.Model):
    bookName = models.CharField(max_length=100, verbose_name=('Book name'))
    bookYear = models.DateField(blank=True, null=True, verbose_name=('Book release year'))
    bookWriter = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name=('Author\'s name'))
    bookDetail = models.TextField(max_length=500, verbose_name=('Book description'))
    borrowedBy = models.CharField(max_length=100, blank=True, null=False, verbose_name=('Borrowed by'))
    borrowedDate = models.DateField(blank=True, null=True, verbose_name=('Borrowed date'))
    isBorrowed = models.BooleanField(default=False, verbose_name=('Currently borrowed'))
    returnedDate = models.DateField(blank=True, null=True, verbose_name=('Return date'))

    # get book url by id
    def get_book_url(self):
        return reverse('book_detail_view', kwargs={'id': self.id})
