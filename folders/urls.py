from django.urls import path

from . import views


app_name = 'folders'

urlpatterns = [
    path('', views.FolderListView.as_view(), name='folder-list'),
    path('add-folder/', views.AddFolderView.as_view(), name='add-folder'),
    path('<pk>/update-folder/', views.UpdateFolderView.as_view(), name='update-folder'),  # noqa
    path('<pk>/add-missing/', views.AddMissingView.as_view(), name='add-missing'),  # noqa
    path('<pk>/update-missing/', views.UpdateMissingView.as_view(), name='update-missing'),  # noqa
]
