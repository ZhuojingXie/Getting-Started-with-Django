from django.contrib import admin
from myblog.models import Post
from myblog.models import Category

class CategoryInline(admin.TabularInline):
        model = Post.categories.through

class PostAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    inlines = [
        CategoryInline,
        ]
admin.site.register(Post,PostAdmin)

class CategoryAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    exclude = ('posts',)
admin.site.register(Category)
