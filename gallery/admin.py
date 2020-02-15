from django.contrib import admin
from .models import Gallery, ImagesList


class GalleryAdmin(admin.ModelAdmin):
    model = Gallery
    list_display = ('name', 'tag', 'published_date')
    list_filter = ['name', 'tag']
    search_fields = ['name', 'tag']


class ImagesListAdmin(admin.ModelAdmin):
    model = ImagesList
    list_display = ('img_link', 'gallery')


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(ImagesList, ImagesListAdmin)
