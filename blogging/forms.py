from django import forms
from .models import Post


# Create your forms here.
class MovieForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "text", "author")
