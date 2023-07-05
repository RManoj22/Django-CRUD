from django import forms
from . models import Products

class Add_stock(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['purchased']
        
class Sub_stock(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['sold']