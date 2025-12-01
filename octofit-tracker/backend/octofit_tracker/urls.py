"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
##from django.contrib import admin
##from django.urls import path

##urlpatterns = [
  ##  path('admin/', admin.site.urls),
#]

import os
from django.contrib import admin
from django.urls import path
from django.http import JsonResponse

# Activities endpoint
def activities_view(request):
    codespace_name = os.environ.get('CODESPACE_NAME', 'localhost')
    api_url = f"https://{codespace_name}-8000.app.github.dev/api/activities/"
    return JsonResponse({
        "message": "Octofit activities endpoint",
        "api_url": api_url
    })

# Root endpoint to fix 404 at '/'
def root_view(request):
    codespace_name = os.environ.get('CODESPACE_NAME', 'localhost')
    return JsonResponse({
        "message": "Welcome to Octofit Tracker API",
        "activities_endpoint": f"https://{codespace_name}-8000.app.github.dev/api/activities/"
    })

# URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/activities/', activities_view),
    path('', root_view),  # <-- Root URL added to fix 404
]
