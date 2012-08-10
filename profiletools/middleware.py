from django.utils.functional import SimpleLazyObject

from profiletools.utils import get_profile, get_my_profile_module_name

# preload this variable
my_profile_module_name = get_my_profile_module_name()


class LazyProfileMiddleware(object):
    """Middleware to attach a lazy .profile value to all requests.
        This reduces the number of queries per request substantially
    """

    def process_request(self, request):
        self.user = request.user
        setattr(request.__class__,
                my_profile_module_name,
                SimpleLazyObject(lambda: get_profile(request.user)))
