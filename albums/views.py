from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView

from ExamPrep_2.utils import get_profile_object
from albums.forms import CreateAlbumForm
from albums.models import Album


# Create your views here.
class AddAlbum(CreateView):
    model = Album
    form_class = CreateAlbumForm
    template_name = 'albums/album-add.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner = get_profile_object()
        return super().form_valid(form)


def details(request):
    return HttpResponse("This is details")


def edit(request):
    return HttpResponse("This is edit")


def delete(request):
    return HttpResponse("This is delete")