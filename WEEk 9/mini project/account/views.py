from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from .models import User
# Create your views here.

def login_page(request):
    form = LoginForm()
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
        message = 'User name or password is invalid .'
    return render(request, 'account/login.html', context={'form': form, 'message': message})

def logout_user(request):
    logout(request)
    return redirect('login')

def register(request):
    #crée une instance du formulaire
    form = RegisterForm()
    #Test l'action si post (envoi de donnée)
    if request.method == 'POST':
        # On recupère les données dans l'instance du formulaire
        form = RegisterForm(request.POST, request.FILES)
        #Verifie si le formulaire est valide
        if form.is_valid():
            #sauvegarde
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect('login_page')
    return render(request, 'account/register.html', context={'form': form})



def users(request):
    user_all = User.objects.all()
    return render(request, 'account/users.html', {"user_all":user_all})
