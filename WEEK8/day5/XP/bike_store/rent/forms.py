from django import forms
from .models import Rental

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['customer', 'vehicle']
        

from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'city', 'country']


class VehicleForm(forms.Form):
    vehicle_type = forms.CharField(max_length=100)
    date_created = forms.DateField()
    real_cost = forms.DecimalField()
    size = forms.CharField(max_length=100)