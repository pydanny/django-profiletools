from django.views.generic import DetailView, UpdateView

from braces.views import LoginRequiredMixin

from profiletools.forms import ProfileForm
from profiletools.utils import get_profile_model

PROFILE_MODEL = get_profile_model()

class ProfileDetailView(LoginRequiredMixin, DetailView):
    
    model = PROFILE_MODEL


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    
    model = PROFILE_MODEL
    form_class = ProfileForm
    success_url = "/my-crazy-profile/"  # You should be using reverse here

    def get_object(self):
        return PROFILE_MODEL.objects.get(user=self.request.user)