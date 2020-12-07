from django import forms

from .models import Folder, Missing


class AddFolderForm(forms.ModelForm):
    class Meta():
        model = Folder
        fields = [
            'owner_id',
            'name',
            'serie',
            'from_date',
            'to_date',
            'from_numeration',
            'to_numeration',
            'code',
        ]


class AddMissingForm(forms.ModelForm):
    class Meta():
        model = Missing
        fields = [
            'folder_id',
            'guide',
        ]
