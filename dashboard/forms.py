from django.core import validators
from django import forms
from .models import Ipconfiguration

class RegistrationIpconfiguration(forms.ModelForm):
    class Meta:
        model=Ipconfiguration
        fields=['id', 'version', 'interface_name','description', 'ip_address', 'net_mask']