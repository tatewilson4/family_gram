from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    name = models.ImageField(upload_to = 'books/', default = 'books/None/no_img.jpg')
    pages = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('book_edit', kwargs={'pk': self.pk})
