from profiletools.utils import get_profile


class LazyProfileMiddleware(object):
    """Middleware to attach a lazy .profile value to all requests.
        This reduces the number of queries per request substantially
    """

    @property
    def lazy_profile(self):
        return get_profile(self.user)

    def process_request(self, request):
        self.user = request.user
        request.__class__.my_profile = self.lazy_profile
