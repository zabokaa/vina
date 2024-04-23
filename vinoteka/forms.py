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
            'shop': 'Bought at',
            'day': 'Date, using YYYY-MM-DD format',
            'occasion': 'Occasion, like Evening with friends, Beach picnic, etc.',
            'rating': 'Rating between 1 (excellent) and 6 (very bad)',
            'pic': 'Picture',
            'memory': 'Memory',
            'foodpairing': 'Food pairing',
            'again': 'Would I buy it again?',
        }
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 6}),
            'day': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
        }

