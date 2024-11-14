from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import BaseFormView
from ExamPrep_2.utils import get_profile_object
from albums.models import Album
from profiles.forms import ProfileBaseForm


# Create your views here.
class HomePageView(BaseFormView, ListView):
    model = Album
    form_class = ProfileBaseForm
    success_url = reverse_lazy('home')

    def get_template_names(self):
        profile = get_profile_object()

        if profile:
            return ['profiles/home-with-profile.html']


        return ['profiles/home-no-profile.html']

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)