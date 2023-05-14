from django.views.generic import CreateView
from django.urls import reverse_lazy
from accounts.forms import CustomUserCreationForm

class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")

# add sign up link to my page so users can sign up and redirect to login page *special patter needed for login* create log in 