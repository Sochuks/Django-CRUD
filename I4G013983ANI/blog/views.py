from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

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
    success_url = "list.html"


class PostListView(ListView):

    # specify the model view for list
    model = Post
    template_name = 'list.html'


class PostDetailView(DetailView):

    # specify the model view for detail
    model = Post
    template_name = 'detail.html'


class PostUpdateView(UpdateView):

    # specify the model view for update
    model = Post

    # Specify fields to be used
    fields = [
        'title',
        'body',
    ]

    template_name = 'update.html'
    success_url = '/'


class PostDeleteView(DeleteView):

    # specify the model you want to use
    model = Post

    template_name = 'delete.html'
    success_url = '/'

