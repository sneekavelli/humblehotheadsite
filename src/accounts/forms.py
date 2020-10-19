from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth import get_user_model
import django.forms as forms

class Form(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email','first_name','last_name','password1','password2')

class ChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email','first_name','last_name')
        widgets = {
            'email':forms.EmailInput(attrs={'readonly':'readonly'})
        }



class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput,required = True)
