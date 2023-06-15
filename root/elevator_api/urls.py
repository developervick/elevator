from django.urls import path, include
from . import views


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('home/', views.home, name="home" )
]