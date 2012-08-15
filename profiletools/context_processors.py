from profiletools.utils import get_my_profile_module_name


def fetch_profile(request):
    """ attaches the user.profile object into the request object"""

    context = {}
    if request.user.is_authenticated():
        profile_module_name = get_my_profile_module_name()
        profile = getattr(request, profile_module_name, None)
        if profile != None:
            context[profile_module_name] = profile
    return context
