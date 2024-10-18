from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View

from posts.forms import AddPostForm, UpdatePostForm
from posts.models import Post


class PostListView(View):
    def get(self, request):
        posts = Post.objects.filter(status='published')
        return render(request, 'posts/list.html', {"posts": posts})


class PostDetailView(View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        return render(request, 'posts/detail.html', {"post": post})


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
