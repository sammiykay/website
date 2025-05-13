
from django.contrib import admin
from django.urls import path, include
from score import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urls)),
]
