from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from PIL import Image
import requests
from io import BytesIO

from books.models import Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'pages']

def book_list(request, template_name='books/book_list.html'):
    book = Book.objects.all()
    data = {}
    data['object_list'] = book
    return render(request, template_name, data)

def book_view(request, pk, template_name='books/book_detail.html'):
    book= get_object_or_404(Book, pk=pk)
    return render(request, {'object':book})

def book_create(request, template_name='books/book_form.html'):
    """form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, template_name, {'form':form})"""

    form = BookForm(request.POST, request.FILES)
    if form.is_valid():
        book = Book.objects.get(pk_course_id)
        book.model_pic = form.cleaned_data['image']
        book.save()
        return redirect('book_list')
    return render(request, template_name, {'form':form})

def book_update(request, pk, template_name='books/book_form.html'):
    book= get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, template_name, {'form':form})

def book_delete(request, pk, template_name='books/book_confirm_delete.html'):
    book= get_object_or_404(Book, pk=pk)
    if request.method=='POST':
        book.delete()
        return redirect('book_list')
    return render(request, template_name, {'object':book})
