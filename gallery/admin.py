from django.contrib import admin
from .models import Gallery


class GalleryAdmin(admin.ModelAdmin):
    model = Gallery
    list_display = ('title', 'name', 'tag', 'published_date')
    list_filter = ['title', 'name', 'tag']
    search_fields = ['name', 'tag']


admin.site.register(Gallery, GalleryAdmin)
