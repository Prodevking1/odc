
from django.urls import path, include
from . import views
urlpatterns = [
    path('home/', views.home, name="home"),
    path('visit/',views.visitor, name="visitor")
]


