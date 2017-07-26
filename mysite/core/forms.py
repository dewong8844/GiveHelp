from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from core.models import Profile
from datetime import date

class EditProfileForm(forms.ModelForm):
    username = forms.CharField(label='Username')
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    driver_license = forms.CharField(label='Driver License')
    driver_license_state = forms.CharField(label='Driver License State')
    license_plate = forms.CharField(label='License Plate')
    license_plate_state = forms.CharField(label='License Plate State')
    photo = forms.ImageField(label='Photo')
    home_address = forms.CharField(label='Home Address')
    home_city = forms.CharField(label='Home City')
    home_state = forms.CharField(label='Home State')
    home_zipcode = forms.CharField(label='Home Zipcode')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'driver_license', 'driver_license_state', 'license_plate', 'license_plate_state', 'photo', 'home_address', 'home_city', 'home_state', 'home_zipcode')

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
        if user_age < 18 and user_type == 'VOLUNTEER':
            raise forms.ValidationError(
                "Volunteer age has to be 18+."
            )
        elif user_age < 60 and (user_type == 'SENIOR' or user_type == 'BOTH'):
            raise forms.ValidationError(
                "Senior age has to be 60+."
            )
        return self.cleaned_data

    class Meta:
        model = User
        fields = ('username', 'user_type', 'email', 'birth_date', 'password1', 'password2', )
