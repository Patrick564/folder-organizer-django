from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import AddFolderForm, AddMissingForm
from .models import Folder, Missing


class FolderListView(LoginRequiredMixin, ListView):
    model = Folder
    context_object_name = 'all_folders'
    template_name = 'folder_list.html'
    paginate_by = 12

    def get_queryset(self):
        all_folders = Folder.objects.filter(
            owner_id=self.request.user.id
        )

        # all_missing = Missing.objects.filter(
        #     folder_id=self.request
        # )

        return all_folders


class AddFolderView(LoginRequiredMixin, CreateView):
    model = Folder
    form_class = AddFolderForm
    template_name = 'add_folder.html'
    success_url = '/folders/'


class UpdateFolderView(LoginRequiredMixin, UpdateView):
    model = Folder
    fields = [
        'serie',
        'from_date',
        'to_date',
        'from_numeration',
        'to_numeration',
        'code',
    ]
    template_name = 'update_folder.html'
    success_url = '/'


# class MissingListView(ListView):
#     model = Missing
#     context_object_name = 'missing_by_folder'
#     template_name = 'missing_list.html'

#     def get_queryset(self):
#         all_missing = Missing.objects.filter(
#             folder_id=self.request.user.id
#         )

#         return all_missing


class AddMissingView(LoginRequiredMixin, CreateView):
    model = Missing
    form_class = AddMissingForm
    template_name = 'add_missing.html'
    success_url = '/'


class UpdateMissingView(LoginRequiredMixin, UpdateView):
    model = Missing
    fields = [
        'guide',
    ]
    template_name = 'update_missing.html'
    success_url = '/'
