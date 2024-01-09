from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import View
from home.forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import UserProfileForm


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        user = authenticate(username=request.POST['username'], password=request.POST['password'])

        if user is not None:
            login(request, user)
            return redirect('user_profile')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})

def logout_view(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # Redirect to the user profile page after successful registration
    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


# def user_profile(request):
#     # Your user profile logic here
#     return render(request, 'user_profile.html')


def user_profile(request):
    if request.method == 'POST':
        # Handle form submission logic here
        # You can access form data using request.POST.get('field_name')
        # For example, you can save the form data to the database

        # Set a success message to be displayed on the user profile page
        success_message = "Application accepted successfully!"
        return render(request, 'user_profile.html', {'success_message': success_message})



    return render(request, 'user_profile.html')

