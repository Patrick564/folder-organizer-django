from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView


urlpatterns = [
    path('', RedirectView.as_view(pattern_name='folders:folder-list')),
    path('accounts/', include('accounts.urls')),
    path('folders/', include('folders.urls')),

    path('admin/', admin.site.urls),
]
