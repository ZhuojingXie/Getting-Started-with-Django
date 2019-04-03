from django.contrib.syndication.views import Feed
from django.urls import reverse
from myblog.models import Post

class LatestEntriesFeed(Feed):
    title = "latest 5 feeds"
    link = "/latest/feed"
    description = "latest 5 feeds"

    def items(self):
        return Post.objects.order_by('-published_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text
