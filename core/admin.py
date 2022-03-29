from django.contrib import admin
from .models import Tag, Article

# Register your models here.

@admin.register(Tag)
class TagView(admin.ModelAdmin):

    model = Tag

@admin.register(Article)
class ArticleView(admin.ModelAdmin):

    model = Article

    list_display = (
        'title',
        'status',
        'date_published',
    )

    list_filter = (
        'status',
        'date_published',
    )

    search_fields = (
        'title',
        'subtitle',
        'slug',
        'meta_description',
    )

    prepopulated_fields = {
        "slug": (
            "title",
        )
    }

    date_hierarchy = 'date_published'

