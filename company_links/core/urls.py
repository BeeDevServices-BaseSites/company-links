from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.index),
    path('logout/', views.logout),
    path('<int:policy_id>/', views.viewPolicy),
    path('createPolicy/', views.createPolicy),
    path('<int:policy_id>/edit/', views.editPolicy),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)