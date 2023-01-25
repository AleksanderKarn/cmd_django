from django.contrib import admin

from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('tittle', 'date_create',)
    prepopulated_fields = {"slug": ("tittle",)}
