from django import forms
from . models import Employeedetails

class Employeeform (forms.ModelForm):
    class Meta:
        model = Employeedetails
        fields = '__all__'
        widgets = {
    'emp_id': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ID :'}),

    'emp_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name :'}),
    
    'emp_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email :'}),

    'emp_designation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Designation :'}),}