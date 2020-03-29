# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView 
from django.views import generic
from .forms import CustomUserCreationForm , CustomUserChangeForm, UpdateProfile
from .models import CustomUser
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserChangeForm
from django.http import HttpResponseRedirect
from django.shortcuts import render


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class Home(generic.ListView):
    model = CustomUser
    context_object_name = "users"
    template_name = 'home.html'
    
'''
class ProfileUser(UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('login')
    template_name = 'edit_profile.html'
    
        
class UserUpdateView(LoginRequiredMixin, UpdateView):
    
    model = CustomUser
    fields = ('address',)
    template_name = 'edit_profile.html'
 '''   

class Profile(generic.ListView):
    model = CustomUser
    template_name = 'profile.html'
           


def edit_profile(request):
    args = {}

    if request.method == 'POST':
        form = UpdateProfile(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/users/profile/')
    else:
        form = UpdateProfile()

    args['form'] = form
    return render(request, 'edit_profile.html', args)
