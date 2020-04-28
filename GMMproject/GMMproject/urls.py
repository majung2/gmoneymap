from django.contrib import admin
from django.urls import path
from odso import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('map/',views.map, name="map"),
]
