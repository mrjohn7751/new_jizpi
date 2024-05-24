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
    return render(request,'institut/__institut.html')

def kengash(request):
    return render(request,'institut/__kengash.html')

def meyoriyHujjat(request):
    return render(request,'institut/__meyoriy-hujjat.html')

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

def OTMkengash(request):
    return render(request,'institut/__kengash-in.html')

def kengash1920(request):
    return render(request,'institut/kengash_19-20.html')

def kengash2021(request):
    return render(request,'institut/kengash_20-21.html')

def kengash2122(request):
    return render(request,'institut/kengash_21-22.html')

def kengash2223(request):
    return render(request,'institut/kengash_22-23.html')

def kengash2324(request):
    return render(request,'institut/kengash_23-24.html')

################################################################################################

def vasiylik(request):
    return render(request,"institut/__vasiylik.html")

def vp1(request):
    return render(request,"institut/vasiylik-page-1.html")

def vp2(request):
    return render(request,"institut/vasiylik-page-2.html")


################################################################################################

def yoshOlimlar(request):
    return render(request,"institut/__yosh-olimlar.html")

def xotinQizlar(request):
    return render(request,"institut/__xotin-qizlar.html")

def ilmiyKengash(request):
    return render(request,"institut/__ilmiy-kengash.html")

################################################################################################

def mhPage1(request):
    return render(request,'institut/mh-page1.html')

def mhPage2(request):
    return render(request,'institut/mh-page2.html')

def mhPage3(request):
    return render(request,'institut/mh-page3.html')

def mhPage4(request):
    return render(request,'institut/mh-page4.html')

def mhPage5(request):
    return render(request,'institut/mh-page5.html')

def mhPage6(request):
    return render(request,'institut/mh-page6.html')

def mhPage7(request):
    return render(request,'institut/mh-page7.html')

def mhPage8(request):
    return render(request,'institut/mh-page8.html')

################################################################################################

def rektorat(request):
    return render(request, 'rektorat/rektorat.html')


def rektor(request):
    return render(request, 'rektorat/rektor.html')

def prYoshlar(request):
    return render(request, 'rektorat/pr-yoshlar.html')

def prOquv(request):
    return render(request, 'rektorat/pr-oquv.html')

def prIlmiy(request):
    return render(request, 'rektorat/pr-ilmiy.html')

def prMoliya(request):
    return render(request, 'rektorat/pr-moliya.html')

def prXalqaro(request):
    return render(request, 'rektorat/pr-xalqaro.html')


################################################################################################
