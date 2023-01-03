from django.shortcuts import render

from django.shortcuts import render
from .models import Family, Animal

def family_view(request, family_id):
    family = Family.objects.get(pk=family_id)
    animals = Animal.objects.filter(family=family)
    context = {'family': family, 'animals': animals}
    return render(request, 'family.html', context)

def animal_view(request, animal_id):
    animal = Animal.objects.get(pk=animal_id)
    context = {'animal': animal}
    return render(request, 'animal.html', context)

def animals_view(request):
    animals = Animal.objects.all()
    context = {'animals': animals}
    return render(request, 'animals.html', context)
