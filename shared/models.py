from django.db import models

from posts.models import Post
from users.models import CustomUser


class View(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='views')
    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return f"{self.user} view {self.post}"

    class Meta:
        unique_together = ('user', 'post')
