"""NoobPaste_DJ URL Configuration

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

from paste_service import views as paste_views
from pages import views as page_views
from auth import views as auth_views

urlpatterns = [
    path('', page_views.home_page, name='home'),
    path('add_paste/', paste_views.create_paste, name='add_paste'),
    path('login/', auth_views.login_page, name="login")
    path('admin/', admin.site.urls),
]
