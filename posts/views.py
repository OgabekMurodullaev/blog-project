from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views import View

from posts.forms import AddPostForm, UpdatePostForm, CommentForm
from posts.models import Post
from shared.utility import record_view, get_most_viewed_this_week, get_most_views_this_month


class PostListView(View):
    def get(self, request):
        posts = Post.objects.filter(status='published')
        return render(request, 'posts/list.html', {"posts": posts})


class PostDetailView(View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        record_view(user=request.user, post=post)
        form = CommentForm()
        return render(request, 'posts/detail.html', {"post": post, "form": form})


class AddPostView(LoginRequiredMixin, View):
    def get(self, request):
        post_form = AddPostForm()
        return render(request, 'posts/add_post.html', {"post_form": post_form})

    def post(self, request):
        post_form = AddPostForm(data=request.POST, files=request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')

        return render(request, 'posts/add_post.html', {"post_form": post_form})


class PostUpdateView(UserPassesTestMixin, View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        edit_form = UpdatePostForm(instance=post)
        return render(request, 'posts/edit.html', {"edit_form": edit_form})

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        edit_form = UpdatePostForm(data=request.POST, instance=post, files=request.FILES)
        if edit_form.is_valid():
            edit_form.save()
            return redirect(reverse('detail', kwargs={"post_id": post.id}))

        return render(request, 'posts/edit.html', {"edit_form": edit_form})

    def test_func(self):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        return post.author == self.request.user


class PostDeleteConfirmView(UserPassesTestMixin, View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        return render(request, 'posts/delete_confirm.html', {"post": post})

    def test_func(self):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        return post.author == self.request.user


class PostDeleteView(UserPassesTestMixin, View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        post.delete()
        messages.success(request, 'You have successfully delete this post')
        return redirect('posts')

    def test_func(self):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        return post.author == self.request.user


class PostCommentCreateView(LoginRequiredMixin, View):
    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect(reverse('detail', kwargs={"post_id": post.id}))

        return render(request, 'posts/detail.html', {"form": form, "post": post})


class MostViewedThisWeekView(View):
    def get(self, request):
        posts = get_most_viewed_this_week()
        return render(request, 'posts/most_viewed_this_week.html', {"posts": posts})


class MostViewedThisMonthView(View):
    def get(self, request):
        posts = get_most_views_this_month()
        return render(request, 'posts/most_viewed_this_month.html', {"posts": posts})

