from django.urls import path
from .views import index, category_list, news, news_detail

urlpatterns = [
    path('',index, name='index'),
    path('yangiliklar/',news,name='news'),
    path('yangiliklar/<int:pk>/',category_list, name='category_list'),
    path('article/<int:pk>/',news_detail,name='ArticleNews_details')
]
