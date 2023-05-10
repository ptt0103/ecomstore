"""user_service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from user_login import views as login_view
from user_model import views as registration_view
from user_info import views as info_view
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_registration/', registration_view.registration_req),
    path('user_login/', login_view.user_login),
    path('user_info/', info_view.user_info),
]
