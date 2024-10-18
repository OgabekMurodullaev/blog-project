from django import forms

from posts.models import Post


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'image', 'tags', 'category')


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'image', 'tags', )
