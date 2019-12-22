from django import forms
from firstapp.models import Customer
class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields="__all__"