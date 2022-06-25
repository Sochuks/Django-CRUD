from django import forms
from .models import Post


# Create Post Forms
class PostForm(forms.ModelForm):

    # Create Meta Class
    class Meta:

        # Specify Models to Be Used
        model = Post

        # Specify fields to be used
        fields = [
            "title",
            "author",
            "body",
        ]
