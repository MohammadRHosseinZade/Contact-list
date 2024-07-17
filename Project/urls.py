from django.contrib import admin
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView 
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include("Accounts.urls")),
    path('contact/', include("Contacts.urls")),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]