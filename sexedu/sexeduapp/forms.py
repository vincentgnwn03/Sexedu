from django import forms  # type: ignore
from django.contrib.auth.models import User  # type: ignore
from sexeduapp.models import Laporan, UserProfileInfo

from .models import Profile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-lg bg-light fs-6',
        'placeholder': 'Buat Password'
    }))

    class Meta():
        model = User
        fields = ('username',  'email', 'password')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control form-control-lg bg-light fs-6',
                'placeholder': 'Masukkan Username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control form-control-lg bg-light fs-6',
                'placeholder': 'Masukkan Email'
            }),
            
        }

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ()



from django import forms  # type: ignore
from django.contrib.auth.forms import UserChangeForm  # type: ignore
from django.contrib.auth.models import User  # type: ignore

from .models import Profile


class UserUpdateForm(UserChangeForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
class LaporanForm(forms.ModelForm):
    class Meta:
        model = Laporan
        fields = ['nama', 'email', 'deskripsi']

