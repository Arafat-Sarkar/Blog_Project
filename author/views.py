from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView
# from .forms import *
from .import forms
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, logout
from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

# Create your views here.



class UserRegistrationView(CreateView):
    template_name = 'registration.html'
    form_class = forms.RegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        confirm_link = f"http://127.0.0.1:8000/author/active/{uid}/{token}"
        email_subject = "Confirm Your Email"
        email_body = render_to_string('confirm_email.html', {'confirm_link' : confirm_link})
        email = EmailMultiAlternatives(email_subject , '', to=[user.email])
        email.attach_alternative(email_body, "text/html")
        email.send()
        messages.success(self.request, 'Check your email for Email Verification🎯')
        # login(self.request, user)
        return super().form_valid(form)
    
def activate(request, uid64, token):
    
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User.objects.get(pk=uid)  
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None 
    
    if user is not None:
        user.is_active = True
        user.save()
        return redirect('login')
    else: 
        print("User not found or token is invalid")
        return redirect('registration')


     
     

# def register(request):
#     if request.method == 'POST':
#         print('post method is passed')
#         register_form = RegistrationForm(request.POST)
#         if register_form.is_valid():
#             print( register_form)
#             register_form.save()
#             messages.success(request, 'Account Created Successfully')
#             return redirect('login')
#         else:
#             print('form is not valid ')
    
#     else:
#         print('form request accpeted')
#         register_form = RegistrationForm()
#     return render(request, 'registration.html', {'form' : register_form, 'type' : 'Register'})
    
    
class UserLoginView(LoginView):
    template_name = 'login.html'
    def get_success_url(self):
        return reverse_lazy('home')
    
class UserLogoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('home')