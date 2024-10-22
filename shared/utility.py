from django.db import models
from django.db.models import Count
from django.utils import timezone

from posts.models import Post
from .models import View


def record_view(user, post):
    View.objects.get_or_create(user=user, post=post)


def get_most_viewed_this_week():
    last_week = timezone.now() - timezone.timedelta(days=7)

    top_posts = (
        Post.objects.filter(views__created_at__gte=last_week).annotate(views_count=Count('views')).order_by('-views_count')[:10]
    )

    return top_posts


def get_most_views_this_month():
    last_month = timezone.now() - timezone.timedelta(days=30)

    top_posts = (
        Post.objects.filter(views__created_at__gte=last_month).annotate(views_count=Count('views')).order_by('-views_count')[:10]
    )

    return top_posts
