from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Person
from .forms import SearchForm


def home(request):
    persons = Person.objects.all()
    return render(request, 'home.html', {'persons': persons})


def search_person(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data.get('query')
            if '+' in query:
                # search by phone number
                return redirect(reverse('person_by_phone', args=[query]))
            else:
                # search by name
                return redirect(reverse('person_by_name', args=[query]))
    else:
        form = SearchForm()
    return render(request, 'person/search_person.html', {'form': form})


def person_by_phone(request, phone_number):

    persons = Person.objects.filter(phone_number=phone_number)
    return render(request, 'results.html', {'persons': persons})


def person_by_name(request, name):

    persons = Person.objects.filter(name__icontains=name)
    return render(request, 'results.html', {'persons': persons})
