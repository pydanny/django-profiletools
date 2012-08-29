from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import get_model


def get_profile(user):

    """ Rather than throw an error on get_profile, we just return None.
        Makes handling of anonymous users in non-loggedin areas easier.
    """
    if user.is_anonymous():
        return None

    try:
        return user.get_profile()
    except ObjectDoesNotExist:
        return None


def get_my_profile_module_name():
    """ Figures out the name of the profile model name from the AUTH_PROFILE_MODULE setting

        Examples:

            my_profile = profiles.Profile
            my_membership = members.Membership
    """
    my_profile_module_name = settings.AUTH_PROFILE_MODULE.split('.')[-1].lower()
    return "my_{0}".format(my_profile_module_name)


def get_profile_model():

    app_name = settings.AUTH_PROFILE_MODULE.split('.')[-2]
    model_name = settings.AUTH_PROFILE_MODULE.split('.')[-1]
    return get_model(app_name, model_name)
