from blogging.models import Post
from django.contrib.syndication.views import Feed
from django.urls import reverse


class LatestPostsFeed(Feed):
    title = "Ben's Django Blog Feed"
    link = "/blogposts/"
    description = "Updates on changes and additions to Ben's blog posts."

    def items(self):
        return Post.objects.order_by("-published_date")[:5]

    def item_title(self, item):
        return item.title

    def item_text(self, item):
        return item.text

    def item_link(self, item):
        return reverse("blog_detail", args=[item.pk])
