from django.contrib import admin


from myblog.models import Post

admin.site.register(Post)

# a new import
from myblog.models import Category

# and a new admin registration
admin.site.register(Category)
