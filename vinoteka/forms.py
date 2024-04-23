from django import forms
from .models import Diary

class DiaryForm(forms.ModelForm):
    """
        A form for creating Diary instances.
        The form includes all fields from the Diary model.
    """
    class Meta:
        model = Diary
        exclude = ['user']
        labels = {
            'wine': 'Wine name',
            'shop': 'Shop',
            'day': 'Date',
            'occasion': 'Occasion',
            'rating': 'Rating',
            'pic': 'Picture',
            'memory': 'Memory',
            'foodpairing': 'Food pairing',
            'again': 'Would you buy it again?',
        }
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }

