from django.shortcuts import render
from django.views import View

from posts.models import Post
from shared.utility import get_most_viewed_posts, get_most_viewed_this_week, get_most_views_this_month


class HomePageView(View):
    def get(self, request):
        latest_posts = Post.objects.filter(status='published').order_by('-created_at')[:2]
        most_viewed_posts = get_most_viewed_posts()[:2]
        most_viewed_this_week = get_most_viewed_this_week()[:2]
        most_viewed_this_month = get_most_views_this_month()[:2]

        context = {
            "latest": latest_posts,
            "most_viewed": most_viewed_posts,
            "weekly": most_viewed_this_week,
            "monthly": most_viewed_this_month
        }
        return render(request, 'landing.html', context)


