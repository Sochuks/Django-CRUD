from django.urls import path

# importing views from views.py
from .views import PostCreateView, PostListView, PostDetailView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostCreateView.as_view(), name='home'),
    path('list/', PostListView.as_view(), name='list'),
    # <pk> is identification for id field
    path('detail/<pk>/', PostDetailView.as_view(), name='detail'),
    path('update/<pk>', PostUpdateView.as_view(), name='update'),
    path('delete/<pk>', PostDeleteView.as_view(), name='delete'),
]