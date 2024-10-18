from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from taggit.managers import TaggableManager

from users.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    body = models.TextField()
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    tags = TaggableManager()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('pending', 'Pending Confirmation'),
        ('published', 'Published')
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return f"{self.title} by {self.author}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment by {self.user}"
