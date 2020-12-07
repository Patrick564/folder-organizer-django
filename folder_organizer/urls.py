from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('folders/', include('folders.urls')),

    path('admin/', admin.site.urls),
]
