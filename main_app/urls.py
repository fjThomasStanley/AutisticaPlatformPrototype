"""
oh_app_demo URL Configuration
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('openhumans/', include('openhumans.urls')),
    path('', include('skeleton.urls')),
    
]

#urlpatterns += [
#    path('openhumans/', include('openhumans.urls')),
#]
