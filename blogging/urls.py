from django.urls import path
from blogging.views import BlogListView, BlogDetailView, BlogAddView
from blogging.feeds import LatestPostsFeed

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_index"),
    path("posts/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("add/", BlogAddView.as_view(), name="blog_add"),
    path("latest/feed/", LatestPostsFeed()),
]
