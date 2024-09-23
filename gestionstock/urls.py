"""
URL configuration for gestionstock project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, reverse_lazy, include
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from inventaire import views as inventaire_views

urlpatterns = [
    # Redirect root URL to the login page
    path('', RedirectView.as_view(url=reverse_lazy('login')), name='root'),

    # Django admin URLs
    path('admin/', admin.site.urls),

    # Authentication-related URLs
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Dashboard URL
    path('dashboard/', inventaire_views.dashboard, name='dashboard'),
    
    # Include inventaire URLs
    path('inventaire/', include('inventaire.urls'))
]


