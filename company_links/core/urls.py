from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.index),
    path('logout/', views.logout),
    path('policy/<int:policy_id>/', views.viewPolicy),
    path('policy/createPolicy/', views.createPolicy),
    path('policy/<int:policy_id>/edit/', views.editPolicy),
    path('document/<int:doc_id>/', views.viewDoc),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)