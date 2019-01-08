from django import forms
#from crudapp.models import Employee
from django.contrib.auth.models import User
from studentapp.models import Student

#from django.contrib.auth.models import User




class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']


class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
