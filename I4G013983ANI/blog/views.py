from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Post


class PostCreateView(CreateView):

    # specify the model to create view
    model = Post

    # Specify fields to be used
    fields = [
        'title',
        'author',
        'body',
    ]

    template_name = 'home.html'


class PostListView(ListView):

    # specify the model view for list
    model = Post
    template_name = 'list.html'

