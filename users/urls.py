from django.urls import path
from django.conf.urls import url

from .views import SignUpView, edit_profile, Profile

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('edit/', edit_profile, name='edit_profile'),
    path('profile/', Profile.as_view(), name='profile'),
    
]
