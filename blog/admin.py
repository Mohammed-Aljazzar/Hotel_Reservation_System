from django.contrib import admin
from tof.admin import TofAdmin, TranslationTabularInline
from tof.decorators import tof_prefetch
from .models import Post, Category


@admin.register(Category)
class CategoryAdmin(TofAdmin):
    list_display = ("id", "name")
    inlines = [TranslationTabularInline]



@admin.register(Post)
class PostAdmin(TofAdmin):
    list_display = ('id', 'title', 'description', 'category')
    search_fields = ('title', )
    inlines = (TranslationTabularInline, )
