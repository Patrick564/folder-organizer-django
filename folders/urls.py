from django.urls import path

from . import views


app_name = 'folders'

urlpatterns = [
    path('', views.FolderListView.as_view(), name='folder-list'),

    path('add-folder/', views.AddFolderView.as_view(), name='add-folder'),
    path('<int:pk>/update-folder/', views.UpdateFolderView.as_view(), name='update-folder'),  # noqa
    path('<int:pk>/delete-folder/', views.DeleteFolderView.as_view(), name='delete-folder'),  # noqa

    path('<int:pk>/missing/', views.MissingListView.as_view(), name='missing-list'),  # noqa
    path('<int:pk>/add-missing/', views.AddMissingView.as_view(), name='add-missing'),  # noqa
    path('<int:pk>/update-missing/', views.UpdateMissingView.as_view(), name='update-missing'),  # noqa
    path('<int:pk>/delete-missing/', views.DeleteMissingView.as_view(), name='delete-missing'),  # noqa
]
