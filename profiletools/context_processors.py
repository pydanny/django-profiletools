def fetch_profile(request):
    """ attaches the user.profile object into the request object"""

    context = {}
    if request.user.is_authenticated():
        profile = request.my_profile
        if profile:
            context['my_profile'] = profile
    return context
