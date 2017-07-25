from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from core.models import Profile
from datetime import date

class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    email = forms.EmailField(max_length=254, help_text='Required. valid email address.')
    user_type = forms.ChoiceField(help_text='Required', choices=Profile.USER_TYPE_CHOICES)

    def age(self, born):
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        
    def clean(self):
        user_type = self.cleaned_data["user_type"]
        user_age = self.age(self.cleaned_data["birth_date"])
        if user_age < 18 and user_type == 'VR':
            raise forms.ValidationError(
                "Volunteer age has to be 18+."
            )
        elif user_age < 60 and (user_type == 'SR' or user_type == 'BH'):
            raise forms.ValidationError(
                "Senior age has to be 60+."
            )
        return self.cleaned_data

    class Meta:
        model = User
        fields = ('username', 'user_type', 'email', 'birth_date', 'password1', 'password2', )
