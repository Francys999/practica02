from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),

    # API JSON
    path('api/', include('tasks.urls')),

    # Redirigir “/” a “/lists/”
    path('', RedirectView.as_view(url='/lists/', permanent=False)),

    # Frontend HTML
    path('', include('tasks.frontend_urls')),
]
