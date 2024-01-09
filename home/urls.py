from django.urls import path
from .views import index, about, register, contact, user_profile, LoginView

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('login/', LoginView.as_view(), name='login'),  # Use LoginView instead of login1
    path('registration/', register, name='register'),
    path('contact/', contact, name='contact'),
    path('user_profile/', user_profile, name='user_profile'),
]
