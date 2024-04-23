from django import forms
from .models import Diary

class DiaryForm(forms.ModelForm):
    """
        A form for creating and updating Diary instances.
        The form includes all fields from the Diary model.
    """
    class Meta:
        model = Diary
        exclude = ['user']