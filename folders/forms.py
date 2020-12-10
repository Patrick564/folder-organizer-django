from django import forms

from .models import Folder, Missing


class AddFolderForm(forms.ModelForm):
    class Meta():
        model = Folder
        fields = [
            'owner',
            'name',
            'serie',
            'from_date',
            'to_date',
            'from_guide',
            'to_guide',
            'code',
        ]


class AddMissingForm(forms.ModelForm):
    class Meta():
        model = Missing
        fields = [
            'folder',
            'guide',
        ]
