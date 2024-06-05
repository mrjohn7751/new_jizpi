from django.contrib import admin
from .models import ArticleNews, ArticleElon, CategoryNews, CategoryElon, ekranImages

admin.site.register(CategoryNews)
admin.site.register(ArticleNews)

admin.site.register(CategoryElon)
admin.site.register(ArticleElon)

admin.site.register(ekranImages)


