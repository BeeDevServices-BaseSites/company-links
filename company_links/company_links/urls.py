from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core import views as app_views
# from user import views as app_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('users/', include('user.urls')),
]
