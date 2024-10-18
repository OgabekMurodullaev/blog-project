from django.urls import path

from posts.views import PostListView, PostDetailView, AddPostView, PostUpdateView

urlpatterns = [
    path('list/', PostListView.as_view(), name='posts'),
    path('new/', AddPostView.as_view(), name='add-post'),
    path('<int:post_id>/', PostDetailView.as_view(), name='detail'),
    path('<int:post_id>/edit/', PostUpdateView.as_view(), name='edit'),

]