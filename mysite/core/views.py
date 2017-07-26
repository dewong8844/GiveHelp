from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from core.forms import SignUpForm, EditProfileForm

def home(request):
    return render(request, 'home.html')

def edit_profile(request):
    user = request.user
    initial_values={'username':user.username, 'driver_license':user.profile.driver_license, 'driver_license_state':user.profile.driver_license_state, 'license_plate':user.profile.car_license_plate, 'license_plate_state':user.profile.car_license_state, 'photo':user.profile.photo, 'home_address':user.profile.home_address, 'home_city':user.profile.home_city, 'home_state':user.profile.home_state, 'home_zipcode':user.profile.home_zipcode}
    form = EditProfileForm(request.POST or None, request.FILES or None, instance=request.user, initial=initial_values)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()  # load the profile instance created by the signal
        user.first_name = form.cleaned_data.get('first_name')
        user.last_name = form.cleaned_data.get('last_name')
        user.profile.birth_date = form.cleaned_data.get('birth_date')
        user.profile.driver_license = form.cleaned_data.get('driver_license')
        user.profile.driver_license_state = form.cleaned_data.get('driver_license_state')
        user.profile.car_license_plate = form.cleaned_data.get('license_plate')
        user.profile.car_license_state = form.cleaned_data.get('license_plate_state')
        user.profile.home_address = form.cleaned_data.get('home_address')
        user.profile.home_city = form.cleaned_data.get('home_city')
        user.profile.home_state = form.cleaned_data.get('home_state')
        user.profile.home_zipcode = form.cleaned_data.get('home_zipcode')
        user.save()
        return redirect('home')

    return render(request, 'edit_profile.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.user_type = form.cleaned_data.get('user_type')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
