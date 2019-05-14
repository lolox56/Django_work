from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm

# Create your views here.


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

# Note that login view function lives inside django.contrib.auth.urls and is tied to /users url at the project level.