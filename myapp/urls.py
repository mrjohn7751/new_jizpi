from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name='index'),
   
    path('yangiliklar/',news,name='news'),
    path('yangiliklar/<int:pk>/',category_list, name='category_list'),
    path('yangiliklar/<int:pk>/',news_detail,name='ArticleNews_details'),
   
    path('elonlar/',elon,name='elon'),
    path('elon/<int:pk>/',category_elon, name='category_elon'),
    path('elon/<int:pk>/',elon_detail,name='ArticleElon_detail'),
    
]
