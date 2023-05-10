"""comment_service URL Configuration

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
from comment_model import views as model_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('insert_comment/', model_views.insertComment_req),
    path('get_comments/', model_views.get_comments),
    path('get_comments_beLongOf/', model_views.get_comments_beLongOf),
]
