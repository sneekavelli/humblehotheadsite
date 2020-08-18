from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import ( 
authenticate, 
get_user_model, 
login, 
logout
)
User = get_user_model()

class ContactForm(forms.Form):
		fullname = forms.CharField(
			widget=forms.TextInput(
				attrs={
				  	   "class": "form-control",
				  	   "placeholder": "Your full name"
				  	   }
				  	   )
	)		

		email 	 = forms.EmailField(
			widget=forms.TextInput(
				attrs={
				"class": "form-control",
				"placeholder": "Your full name"
				}
				)
			)
		content  = forms.CharField(
			widget=forms.Textarea(attrs={'class': 'form-control', "placeholder": "Your content"}
				)
			)

	 #def clean_email(self):
		 #email = self.cleaned_data.get("email")
			#if not "gmail.com" in email:
				#raise forms.ValidationError("Email must be gmail.com")
			#return email

class LoginForm(forms.Form):
		username = forms.CharField()
		password = forms.CharField(widget=forms.PasswordInput)



def clean(self, *args, **kwargs):
			username = self.cleaned_data.get('username')
			password = self.cleaned_data.get('password')

			if username and password: 
				user = authenticate(username=username, password=password)
				if not user:
					raise forms.ValidationError('This user does not exist')
				if not user.check_password(password): 
					raise forms.ValidationError('Incorrect password')
				if not user.is_active:
					raise forms.ValidationError('This user is not active')
			return super(LoginForm, self).clean(*args,**kwargs)


class RegisterForm(UserCreationForm):
    	first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    	last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    	email = forms.EmailField(max_length=254, help_text=' Inform a valid email address.')
class Meta:
		 model = User
		 fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


# """ 	def clean_username(self):
# 		username = self.cleaned_data.get('username')
# 		qs = user.objects.filter(username=username)
# 		if qs.exists():
# 		return username 
# 			 raise forms.ValidationError("Username is taken")
#  """
	
#	def clean(self):
#		password = self.cleaned_data.get('password')
#		data = self.cleaned_data
#		password2 = self.cleaned_data.get('password2')
###		if password2 != password:
#			raise forms.ValidationError("Passwords must match.")
#		return data

	 


	



	 






