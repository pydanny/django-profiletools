from django.conf.urls.defaults import patterns, url

from profiletools import views

urlpatterns = patterns("",
    url(regex=r'^my-crazy-profile/$',
        view=views.ProfileUpdateView.as_view(),
        name='profile_update'),
)