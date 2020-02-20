from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('contenuto',)
    list_display = ('titolo', 'tag', 'published_date')
    list_filter = ['titolo', 'tag']
    search_fields = ['titolo', 'tag']


admin.site.register(Post, PostAdmin)
