from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

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

        return all_folders


class AddFolderView(LoginRequiredMixin, CreateView):
    model = Folder
    form_class = AddFolderForm
    template_name = 'add_folder.html'
    success_url = '/folders/'


class UpdateFolderView(LoginRequiredMixin, UpdateView):
    model = Folder
    fields = [
        'name',
        'serie',
        'from_date',
        'to_date',
        'from_guide',
        'to_guide',
        'code',
    ]
    template_name = 'update_folder.html'
    success_url = '/folders/'


class DeleteFolderView(LoginRequiredMixin, DeleteView):
    model = Folder
    template_name = 'delete_folder.html'
    success_url = '/folders/'


class MissingListView(ListView):
    model = Missing
    context_object_name = 'all_missing'
    template_name = 'missing_list.html'

    def get_queryset(self):
        all_missing = Missing.objects.filter(
            folder=self.kwargs['pk']
        )

        return all_missing


class AddMissingView(LoginRequiredMixin, CreateView):
    model = Missing
    form_class = AddMissingForm
    template_name = 'add_missing.html'

    def get_success_url(self):

        return reverse(
            'folders:missing-list',
            kwargs={'pk': self.kwargs['pk']}
        )


class UpdateMissingView(LoginRequiredMixin, UpdateView):
    model = Missing
    fields = [
        'guide',
    ]
    template_name = 'update_missing.html'

    def get_success_url(self):
        self.missing = self.get_object().folder
        self.folder = Folder.objects.get(code=self.missing)

        return reverse(
            'folders:missing-list',
            kwargs={'pk': self.folder.id}
        )


class DeleteMissingView(LoginRequiredMixin, DeleteView):
    model = Missing

    def delete(self, *args, **kwargs):
        self.missing = self.get_object().folder
        self.folder = Folder.objects.get(code=self.missing)

        return super(DeleteMissingView, self).delete(*args, **kwargs)

    def get_success_url(self):

        return reverse(
            'folders:missing-list',
            kwargs={'pk': self.folder.id}
        )
