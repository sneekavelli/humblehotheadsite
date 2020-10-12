import django.forms as forms
from .models import Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        exclude = ('user',)
        widgets = {
            'address':forms.Textarea(attrs={'rows':'2'})
        }
