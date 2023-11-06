from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('CNIT581-048-Milestone3', views.video, name='homepage'),
    path('', views.video, name='default'),
    path('annotationList', views.list, name='annotationList'),
    path('video', views.video, name='annotationVideo'),
    path('addAnnotation', views.addAnnotation, name='addAnnotation'),
    path('viewAnnotation', views.viewAnnotation, name='viewAnnotation'),
    path('editAnnotation', views.editAnnotation, name='editAnnotation'),
    path("admin/", admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls")),
]

# Login tutorial taken from this site: https://learndjango.com/tutorials/django-login-and-logout-tutorial
# I used BingAI for finding out which django file does what because I don't know how define my settings and which file to define them in