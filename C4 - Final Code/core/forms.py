from django import forms
from core.models import User


class UserSettingsForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'profile_picture')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input input-bordered'}),
            'last_name': forms.TextInput(attrs={'class': 'input input-bordered'}),
            'profile_picture': forms.FileInput(attrs={'class': 'file-input'})
        }