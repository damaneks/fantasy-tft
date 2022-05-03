from django.contrib.auth import forms
from django.contrib.auth import get_user_model
from django_countries.fields import CountryField

User = get_user_model()


class RegisterForm(forms.UserCreationForm):
    country = CountryField().formfield()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'country']

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control mx-sm-3'})


class LoginForm(forms.AuthenticationForm):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control mx-sm-3'})
