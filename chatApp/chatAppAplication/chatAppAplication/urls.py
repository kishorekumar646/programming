"""chatAppAplication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from user_interface.views import RegistrationAPI,LoginAPI,activate,chat_page,UserAPI,ForgotPasswordAPI,reset_password,ResetPassword

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',RegistrationAPI.as_view()),
    path('login/',LoginAPI.as_view(),name="login"),
    path('format-api/',UserAPI.as_view()),
    path('chat_page/',chat_page),
    path('activate/<slug:surl>',activate, name='activate'),
    path('forgotpassword/',ForgotPasswordAPI.as_view(),name="forgotpassword"),

    path('reset_password/<slug:surl>/', reset_password, name="reset_password"),
    path('resetpassword/', ResetPassword.as_view(), name="resetpassword"),
]
