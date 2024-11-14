from django import forms
from ExamPrep_2.mixins import PlaceholderMixin
from albums.models import Album


class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ('owner', )


class CreateAlbumForm(AlbumBaseForm, PlaceholderMixin):
    pass