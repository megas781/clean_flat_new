from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
#нужно еще создать и импортировать форму
from django.urls import reverse_lazy, reverse
#from django.contrib import messages

#для наследования классам
from django.contrib.auth.views import LoginView, LogoutView
# нужно для создания пользователя (при реги страции)
from django.contrib.auth.forms import User
from .forms import CustomAuthUserForm, CustomRegisterUserForm
from django.contrib.auth import authenticate, login

#Мутим страницу авторизации через классы
class CustomLoginView (LoginView):
    template_name = 'login/login.html'
    form_class = CustomAuthUserForm
    success_url = '/'

# нужно для переадресации после входа
    def get_success_url(self):
        return self.success_url
    # template_name = 'login/register.html'
    # form_class = CustomRegisterUserForm
    # success_url = reverse_lazy('edit-page')
    # success_msg = 'Регистрация прошла успешно'

class CustomRegisterView(CreateView):
    template_name = 'login/register.html'
    form_class = CustomRegisterUserForm
    success_url = '/'
    success_msg = 'Регистрация прошла успешно'
    def form_valid(self, form):
        form_valid = super().form_valid(form=form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        auth_user = authenticate(username=username, password=password)
        login(self.request, auth_user)
        return form_valid

class CustomLogoutView(LogoutView):
    next_page = '/login'