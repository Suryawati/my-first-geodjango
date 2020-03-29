from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from users import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path("", views.Home.as_view(template_name='home.html'), name='home'),
]


