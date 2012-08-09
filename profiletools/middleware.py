from profiletools.utils import get_profile, get_my_profile_module_name


class LazyProfileMiddleware(object):
    """Middleware to attach a lazy .profile value to all requests.
        This reduces the number of queries per request substantially
    """

    @property
    def lazy_profile(self):
        return get_profile(self.user)

    def process_request(self, request):
        self.user = request.user
        setattr(request.__class__, get_my_profile_module_name(), self.lazy_profile)
