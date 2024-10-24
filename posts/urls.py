from django.urls import path

from posts.views import (PostListView, PostDetailView, AddPostView,
                         PostUpdateView, PostDeleteConfirmView, PostDeleteView,
                         PostCommentCreateView)


urlpatterns = [
    path('list/', PostListView.as_view(), name='posts'),
    path('new/', AddPostView.as_view(), name='add-post'),
    path('<int:post_id>/', PostDetailView.as_view(), name='detail'),
    path('<int:post_id>/comments/', PostCommentCreateView.as_view(), name='add-comment'),
    path('<int:post_id>/edit/', PostUpdateView.as_view(), name='edit'),
    path('<int:post_id>/confirm-delete/', PostDeleteConfirmView.as_view(), name='confirm-delete'),
    path('<int:post_id>/delete/', PostDeleteView.as_view(), name='delete'),
]