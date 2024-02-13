from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse

def Tracker(request):
    return HttpResponse("HELLOW WORLD!")

from django.http import HttpResponse
from django.template import loader

def Tracker(request):
    template=loader.get_template('myFirst.html')
    return HttpResponse(template.render())

from django.shortcuts import render
from.models import BookCategory
from.forms import BookCategoryForm

def list_category(request):
    categories=BookCategory.objects.all()
    return render(request,'list_category.html',{'categories':categories})

from django.shortcuts import render, redirect
from .forms import BookCategoryForm

def create_category(request):
    form = BookCategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_category')
    return render(request, 'category_form.html', {'form': form})

def update_category(request, id):
    category = BookCategory.objects.get(id=id)
    form = BookCategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect('list_category')
    return render(request, 'category_form.html', {'form': form, 'category': category})

def delete_category(request, id):
    category = BookCategory.objects.get(id=id)
    if request.method == 'POST':
        category.delete()
        return redirect('list_category')
    return render(request, 'category_delete_confirm.html', {'category': category})

from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book

def read (request):
    books = Book.objects.all()
    return render(request, 'read.html', {'books': books})

def create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('read')
    return render(request, 'create.html', {'form': form})

def update(request, id):
    book = Book.objects.get(id=id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('read')
    return render(request, 'create.html', {'form': form, 'book': book})

def delete(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('read')
    return render(request, 'delete_confirm.html', {'book': book})

# Create your views here.