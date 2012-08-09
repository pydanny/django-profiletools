from profiletools.utils import get_my_profile_module_name


def fetch_profile(request):
    """ attaches the user.profile object into the request object"""

    context = {}
    if request.user.is_authenticated():
        profile = request.my_profile
        if profile:
            context[get_my_profile_module_name()] = profile
    return context
