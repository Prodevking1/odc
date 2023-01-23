from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Visitor, Bedroom_type, Bedroom_size, Bedroom, Book, Review, Simple_Reviews
from .forms import VisitorForm, Bedroom_sizeForm, Bedroom_typeForm, BookForm, BedroomForm, ReviewForm, Simple_reviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def home(request):
    return render(request, 'visitors/homeAdmin.html')
@login_required
def visitor(request):
    visitor = Visitor.objects.all()
    visit_atr = Visitor.objects.first()
    form = VisitorForm()
    return render(request, 'visitors/visitors.html', {'models': visitor, 'atributs':visit_atr, 'form': form})
@login_required
def bedroom(request):
    bedroom = Bedroom.objects.all()
    form = BedroomForm()
    return render(request, 'visitors/bedroom.html', {'models': bedroom, 'form': form})
@login_required
def bedroom_size(request):
    bedroom_size = Bedroom_size.objects.all()
    form = Bedroom_sizeForm()
    return render(request, 'visitors/bedroom_size.html', {'models': bedroom_size, 'form': form})

def bedroom_type(request):
    bedroom_type = Bedroom_type.objects.all()
    form = Bedroom_typeForm()
    return render(request, 'visitors/bedroom_type.html', {'models': bedroom_type, 'form': form})
@login_required
def book(request):
    book = Book.objects.all()
    form = BookForm()
    return render(request, 'visitors/book.html', {'models': book, 'form': form})

@login_required
def review(request):
    review = Review.objects.all()
    form = ReviewForm()
    return render(request, 'visitors/review.html', {'models': review, 'form': form})
@login_required
def simple_review(request):
    simple_review = Simple_Reviews.objects.all()
    form = Simple_reviewForm()
    return render(request, 'visitors/visitor.html', {'models': visitor, 'form': form})