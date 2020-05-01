from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from odso import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # templates
    path('', views.HomeView.as_view(), name='home'),
    path('map/', views.MapView.as_view(), name='map'),

    # rest api (json)
    path('api/v1/cities/', views.CityList.as_view()),
    path('api/v1/cities/<int:pk>/', views.CityDetail.as_view()),
    path('api/v1/stores/', views.StoreList.as_view()),
    path('api/v1/stores/<str:pk>/', views.StoreDetail.as_view()),

    path('healthy-check/', views.HealthyCheckView.as_view()),
]

# static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
