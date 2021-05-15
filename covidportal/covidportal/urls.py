"""covidportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    url(r'^accounts/', include('django.contrib.auth.urls')),
    path('beds/', include('beds.urls')),
    path('admin/', admin.site.urls),
]

'''
accounts/login/ is used to log a user into your application. Refer to it by the name "login".

accounts/logout/ is used to log a user out of your application. Refer to it by the name "logout".

accounts/password_change/ is used to change a password. Refer to it by the name "password_change".

accounts/password_change/done/ is used to show a confirmation that a password was changed. Refer to it by the name "password_change_done".

accounts/password_reset/ is used to request an email with a password reset link. Refer to it by the name "password_reset".

accounts/password_reset/done/ is used to show a confirmation that a password reset email was sent. Refer to it by the name "password_reset_done".

accounts/reset/<uidb64>/<token>/ is used to set a new password using a password reset link. Refer to it by the name "password_reset_confirm".

accounts/reset/done/ is used to show a confirmation that a password was reset. Refer to it by the name "password_reset_complete".


'''
