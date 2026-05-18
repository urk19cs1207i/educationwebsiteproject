from django import forms
from app1.models import Employee
from app1.models import Parent
from app1.models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee 
        fields='__all__' 

class ParentForm(forms.ModelForm):
    class Meta:
        model=Parent
        fields='__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'


class SignupForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = ['username', 'email', 'password', 'first_name', 'last_name']
