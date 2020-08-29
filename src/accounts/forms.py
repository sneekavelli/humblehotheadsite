from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
import django.forms as forms

class Form(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email','first_name','last_name','password1','password2','portfolio_site','profile_pic')


class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput,required = True)
