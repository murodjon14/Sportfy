"""
URL configuration for core project.

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
from django.contrib import admin
from django.urls import path, include
from main.views import *
from rest_framework.routers import DefaultRouter

# router = DefaultRouter

# router.register('qoshiqchi_albomlari', QoshiqchilarModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('qoshiqchilar/', QoshiqchilarAPIView.as_view()),
    path('qoshiqchi/<int:pk>/update', QoshiqchiUpdatingAPIView.as_view()),
    path('qoshiqchi/<int:pk>/delete', QoshiqchiDeleteAPIView.as_view()),
    # path('', include(router.urls))
]
