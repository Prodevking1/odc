"""bike_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rent import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.rental_list),
    path('faker/', views.generate_fake_data, name='generate_fake_data'),
    path('rent/rental/', views.rental_list, name='rental_list'),
    path("rent/rental/add", views.add_rental, name="add_rental"),
    path('rental/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('rent/customer/', views.CustomerListView.as_view(), name='customer_list'),
    path('rent/customer/add', views.add_customer, name='add_customer'),
    path('rent/vehicle/', views.show_vehicles, name='show_vehicles'),
    path('rent/vehicle/<int:pk>/', views.vehicle_detail, name='vehicle_detail'),


]
