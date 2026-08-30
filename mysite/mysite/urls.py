"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

try:
    from service.views import system_demo
except ImportError:
    # Define a fallback view if service.views can't be imported during build
    def system_demo(request):
        from django.http import HttpResponse
        return HttpResponse("System demo not available during build phase")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('t/<slug:tenant_slug>/<int:tenant_id>/<str:tenant_key>/', include(('service.urls', 'service'), namespace='tenant_service')),
    path('t/<slug:tenant_slug>/<int:tenant_id>/<str:tenant_key>/', include('core.urls')),
    path('', include('core.urls')),
    path('system/', system_demo, name='system_demo'),
    path('service/', include(('service.urls', 'service'), namespace='service')),
    path('service/', include('core.urls')),
]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.BASE_DIR / 'static')
