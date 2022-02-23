from django.contrib import admin
from django.urls import path
from core.views import foo

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", foo),
]
