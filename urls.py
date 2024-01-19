# house_price_prediction/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prediction/', include('prediction.urls')),
]
