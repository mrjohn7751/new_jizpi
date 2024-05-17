from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    ekranImg = ekranImages.objects.all()
    Category_news = CategoryNews.objects.all()
    Article_news = ArticleNews.objects.all()
    Category_elon = CategoryElon.objects.all()
    Article_elon = ArticleElon.objects.all()
    Category_facultet = CategoryFacultet.objects.all()
    Article_facultet = ArticleFacultet.objects.all()

    context = {
        'ekranImg':ekranImg,
        'Category_news':Category_news,
        'Article_news':Article_news,
        'Category_elon':Category_elon,
        'Article_elon':Article_elon,
        'Category_facultet':Category_facultet,
        'Article_facultet':Article_facultet,
    }
    return render(request,'index.html',context)



def category_list(request,pk):
    Category_news = CategoryNews.objects.all()
    Article_news = ArticleNews.objects.all()
    context = {
        'Category_news':Category_news,
        'Article_news':Article_news,  
    }
    return render(request,'news/news.html',context)

def category_elon(request,pk):
    Category_elon = CategoryElon.objects.all()
    Article_elon = ArticleElon.objects.all()
    context = {
        'Category_elon':Category_elon,
        'Article_elon':Article_elon, 
    }
    return render(request,'news/elon.html',context)


def news(request):
    Category_news = CategoryNews.objects.all()
    Article_news = ArticleNews.objects.all()
    context = {
        'Category_news':Category_news,
        'Article_news':Article_news,
    }
    return render(request,'news/news.html',context)


def news_detail(request,pk):
    Article_news = ArticleNews.objects.get(pk=pk)
    context = {
        'article':Article_news,
    }
    return render(request,'news/news-in.html',context)



def elon(request):
    Category_elon = CategoryElon.objects.all()
    Article_elon = ArticleElon.objects.all()
    context = {
        'Category_elon':Category_elon,
        'Article_elon':Article_elon,
    }
    return render(request,'news/elon.html',context)


def elon_detail(request,pk):
    Article_elon = ArticleElon.objects.get(pk=pk)
    context = {
        'Article_elon':Article_elon,
    }
    return render(request,'news/elon-in.html',context)

################################################################################################
# Instut hamma pagelari

def institut(request):
    return render(request,'institut/institut.html')

def institutPage_1(request):
    return render(request,'institut/instut-page1.html')

def institutPage_2(request):
    return render(request,'institut/instut-page2.html')

def institutPage_3(request):
    return render(request,'institut/instut-page3.html')

def institutPage_4(request):
    return render(request,'institut/instut-page4.html')

def institutPage_5(request):
    return render(request,'institut/instut-page5.html')

def institutPage_6(request):
    return render(request,'institut/instut-page6.html')

def institutPage_7(request):
    return render(request,'institut/instut-page7.html')

################################################################################################
