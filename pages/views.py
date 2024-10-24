from django.core.paginator import Paginator
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


class LatestPostsView(View):
    def get(self, request):
        latest_posts = Post.objects.filter(status='published').order_by('-created_at')
        paginator = Paginator(latest_posts, 4)
        page_number = request.GET.get('page', 1)
        posts = paginator.get_page(page_number)
        return render(request, 'posts/latest_posts.html', {"posts": posts})


class MostViewedThisWeekView(View):
    def get(self, request):
        most_viewed_this_week = get_most_viewed_this_week()
        paginator = Paginator(most_viewed_this_week, 4)
        page_number = request.GET.get('page', 1)
        posts = paginator.get_page(page_number)
        return render(request, 'posts/most_viewed_this_week.html', {"posts": posts})


class MostViewedThisMonthView(View):
    def get(self, request):
        most_viewed_this_month = get_most_views_this_month()
        paginator = Paginator(most_viewed_this_month, 4)
        page_number = request.GET.get('page', 1)
        posts = paginator.get_page(page_number)
        return render(request, 'posts/most_viewed_this_month.html', {"posts": posts})


class MostViewedAllTimeView(View):
    def get(self, request):
        most_viewed_posts = get_most_viewed_posts()
        paginator = Paginator(most_viewed_posts, 4)
        page_number = request.GET.get('page', 1)
        posts = paginator.get_page(page_number)
        return render(request, 'posts/most_viewed_posts.html', {"posts": posts})




