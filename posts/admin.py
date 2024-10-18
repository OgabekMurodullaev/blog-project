from django.contrib import admin

from posts.models import Category, Post, Comment


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'status')
    search_fields = ('title', 'author', 'category')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment', 'created_at')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
