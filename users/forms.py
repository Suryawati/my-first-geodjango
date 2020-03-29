from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

from django.contrib.gis.forms import OSMWidget

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        #fields = ('username', 'email', 'age',)
        
        fields = UserCreationForm.Meta.fields + ('address','phone_number','is_staff','location',)
        widgets = {
           'location': OSMWidget(
                attrs={
                    'map_width': 1400,
                    'map_height': 400,
                    'default_lat': -7.1214355,
                    'default_lon': 113.312767,
                    'default_zoom': 12
                }
            )
            }
        


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'address', 'phone_number', 'location')
        


class UpdateProfile(forms.ModelForm):
    username = forms.CharField(required=True)
    

    class Meta:
        model = CustomUser
        fields = ('username', 'address', 'phone_number', 'location')
        widgets = {
           'location': OSMWidget(
                attrs={
                    'map_width': 1400,
                    'map_height': 400,
                    'default_lat': -7.1214355,
                    'default_lon': 113.312767,
                    'default_zoom': 12
                }
            )
            }

    