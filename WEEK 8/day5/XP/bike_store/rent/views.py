from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer, Rental, Vehicle
from .forms import CustomerForm, RentalForm, VehicleForm
from django.views.generic import ListView
from .models import Customer
from faker import Faker

fake = Faker()

def generate_fake_data(request):
    for i in range(10):
        customer = Customer(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            phone_number=fake.phone_number(),
            address=fake.address(),
            city=fake.city(),
            country=fake.country()
        )
        customer.save()

    return render(request, 'faker.html')

def rental_list(request):
    rentals = Rental.objects.filter(return_date__isnull=True).order_by('rental_date') | Rental.objects.exclude(return_date__isnull=True).order_by('rental_date')
    return render(request, 'rental_list.html', {'rentals': rentals})

def rental_detail(request, pk):
    rental = get_object_or_404(Rental, pk=pk)
    context = {
        'rental': rental,
        'customer': rental.customer,
        'vehicle': rental.vehicle
    }
    return render(request, 'rental_detail.html', context)


def add_rental(request):
    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            customer_id = form.cleaned_data['customer']
            vehicle_id = form.cleaned_data['vehicle']
            # Vérifiez si le client et le véhicule existent
            try:
                customer = Customer.objects.get(pk=customer_id)
                vehicle = Vehicle.objects.get(pk=vehicle_id)
            except Customer.DoesNotExist:
                return render(request, 'add.html', {'form': form, 'error_message': 'Le client n\'existe pas.'})
            except Vehicle.DoesNotExist:
                return render(request, 'add.html', {'form': form, 'error_message': 'Le véhicule n\'existe pas.'})
            # Vérifiez si le véhicule est déjà loué
            if vehicle.rental_set.filter(return_date__isnull=True).exists():
                return render(request, 'add.html', {'form': form, 'error_message': 'Le véhicule est déjà loué.'})
            # Créez une nouvelle location
            rental = Rental(customer=customer, vehicle=vehicle)
            rental.save()
            return redirect('rental_list')
    else:
        form = RentalForm()
    return render(request, 'add.html', {'form': form})

def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'customer_detail.html', {'customer': customer})


class CustomerListView(ListView):
    model = Customer
    context_object_name = 'customers'
    template_name = 'customer_list.html'

    def get_queryset(self):
        return Customer.objects.all().order_by('last_name')


def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'customer_add.html', {'form': form})

def show_vehicles(request):
    vehicles = Vehicle.objects.all()
    groups = {}
    for v in vehicles:
        if v.vehicle_type not in groups:
            groups[v.vehicle_type] = [v]
        else:
            groups[v.vehicle_type].append(v)
    return render(request, 'vehicles.html', {'groups': groups})


def vehicle_detail(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    return render(request, 'vehicle_detail.html', {'vehicle': vehicle})

def add_vehicle(request):
    form = VehicleForm()
    return render(request, 'add_vehicle.html', {'form': form})