from django.contrib import admin

from .models import Todo
from .models import Categorie

admin.site.register(Todo)
admin.site.register(Categorie)
