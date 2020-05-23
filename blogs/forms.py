from django import forms

from .models import BlogPost, Entry

class BlogPostForm(forms.ModelForm):
    """Creates a blank form for accepting the Blogpost title."""
    class Meta:
        model = BlogPost
        fields = ['title']
        labels = {'title': ''}


class EntryForm(forms.ModelForm):
    """Creates a form to accept the Content a Blogpost created."""
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}


