from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BlogPost(models.Model):
    """A model for creating a blog post."""
    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Returns a string representation of the model."""
        return self.title


class Entry(models.Model):
    """A model for adding text(entry) for the model BlogPost."""
    blogpost = models.ForeignKey(BlogPost, on_delete=models.Model)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Returns a string representation of the model EntryPost."""
        return self.text



