"""
URL configuration for drfsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from women.views import WomanViewSet, index
from rest_framework import routers

router = routers.SimpleRouter()
router.register('women', WomanViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    """ Ниже пути, которые были до введения роутеров и вью-сета"""
    # path('api/v1/women/', WomanViewSet.as_view({'get': 'list'}), name='women'),
    # path('api/v1/women/<int:pk>/', WomanViewSet.as_view({'put': 'update'})),
]
