from django.urls import path

# importing views from views.py
from .views import PostCreateView, PostListView

urlpatterns = [
    path('', PostCreateView.as_view(), name='home'),
    path('list/', PostListView.as_view(), name='list')
]