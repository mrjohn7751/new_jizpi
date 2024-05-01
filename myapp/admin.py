from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(ekranImages)

admin.site.register(CategoryNews)
admin.site.register(ArticleNews)

admin.site.register(CategoryElon)
admin.site.register(ArticleElon)

admin.site.register(CategoryFacultet)
admin.site.register(ArticleFacultet)
