from django import forms
from service.models import Service
from django.contrib.auth.forms import User, AuthenticationForm


#здесь будет еще объявлена форма ServiceForm...

#это класс формы
class ServiceForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
    # def __init__(self, args, kwargs):
    #     super.__init__(self,args,kwargs)
    #     for field in self.fields:
    #         self.fields[field].widget.attrs['class'] = 'form-control'


class CustomAuthUserForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class CustomRegisterUserForm(forms.ModelForm):
    #шифровение паролей, чтобы пользователь работал
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'password']


