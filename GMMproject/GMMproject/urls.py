"""GMMproject URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from odso import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # templates
    path('', views.HomeView.as_view()),
    path('map/', views.MapView.as_view()),

    # rest api (json)
    path('api/v1/cities/', views.CityList.as_view()),
    path('api/v1/cities/<int:pk>/', views.CityDetail.as_view()),
    path('api/v1/stores/', views.StoreList.as_view()),
    path('api/v1/stores/<str:pk>/', views.StoreDetail.as_view()),
]

# static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
