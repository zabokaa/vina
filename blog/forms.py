from django import forms
from .models import Comment



class CommentForm(forms.ModelForm):
    """
        A form for creating and updating Comment instances.
        The form includes only the 'body' field from the Comment model.
    """
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {
            'body': 'Type your note, and hit submit!',
        }
