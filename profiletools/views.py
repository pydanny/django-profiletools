from django.core.urlresolvers import reverse
from django.views.generic import DetailView, UpdateView

from braces.views import LoginRequiredMixin

from profiletools.forms import ProfileForm
from profiletools.utils import get_profile_model

PROFILE_MODEL = get_profile_model()

class ProfileDetailView(LoginRequiredMixin, DetailView):
    
    model = PROFILE_MODEL


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """ Called thus with a slug::

            url(regex=r'^/(?P<slug>[\_-\w]+)/$',
                view=views.ProfileUpdateView.as_view(
                    success_url="/",
                ),
                name='profile_update'),

        Or thus with an ID::

            url(regex=r'^/(?P<id>\d+)/$',
                view=views.ProfileUpdateView.as_view(
                    success_url="/",
                ),
                name='profile_update'),

    """

    model = PROFILE_MODEL
    form_class = ProfileForm


class ProfileUpdateNoSlugView(ProfileUpdateView):
    """ Called thus::
            url(regex=r'^edit-my-crazy-profile/$',
                view=views.ProfileUpdateView.as_view(
                    success_url="edit-my-crazy-profile",
                ),
                name='profile_update'),
    """

    def get_object(self):
        return PROFILE_MODEL.objects.get(user=self.request.user)


class DefaultProfileUpdateNoSlugView(LoginRequiredMixin, UpdateView):

    def get_object(self):
        profile, created = PROFILE_MODEL.objects.get_or_create(
            user=self.request.user
        )
        return profile