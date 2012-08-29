from django import forms

from profiletools.utils import get_profile_model

PROFILE_MODEL = get_profile_model()


class ProfileForm(forms.ModelForm):

    class Meta:
        model = PROFILE_MODEL
        exclude = getattr(PROFILE_MODEL, "exclude", ('user', ))
        fields = getattr(PROFILE_MODEL, "fields", ())        
