from django.contrib import admin

from book.app.Infrastructure.models import Book


# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    readonly_fields = ("id", 'slug')
    list_display = ('id','title', 'author', 'is_published', 'updated_at')
    list_display_links = ('id', 'title')
    list_per_page = 10
    search_fields = ('title',)

# admin.site.register(models.Book)