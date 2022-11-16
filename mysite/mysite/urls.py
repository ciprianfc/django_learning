"""mysite URL Configuration

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
from django.urls import path, include
from django.views.static import serve

urlpatterns = [
    # this will create warning, we already use gview
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('route/', include('route.urls', namespace='nsroutes')),
    path('getpost/', include('getpost.urls')),
    path('session/', include('session.urls')),
    path('gview/', include('gview.urls')),
    path('hello/', include('hello.urls')),
    path('authz/', include('authz.urls')),
    path('form/', include('form.urls')),
    path('autos/', include('autos.urls')),
    path('myarts/', include('myarts.urls')),
    path('crispy/', include('crispy.urls')),
    path('menu/', include('menu.urls')),
    path('pics/', include('pics.urls')),
    path('forums/', include('forums.urls')),
    path('chat/', include('chat.urls'))
]

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_URL = 'static/'

STATIC_ROOT = Path().joinpath(BASE_DIR,'home',STATIC_URL)
# server the favinco
urlpatterns += [
    path('favicon.ico', serve, {
        'path' : 'favicon.ico',
        'document_root' : STATIC_ROOT,
    })
]
