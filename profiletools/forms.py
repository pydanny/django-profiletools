from django import forms

from profiletools.utils import get_profile_model

class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = get_profile_model()
        exclude = ('user', )

