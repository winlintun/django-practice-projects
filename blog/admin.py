from django.contrib import admin
from .models import Post, Tag, Category, Comment


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title', )}
    list_display = ("title", "slug", "status", "created_on")
    list_filter = ("status",)
    search_fields = ['title', 'content']


admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
