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
    return render(request, 'rektorat/rektorat/rektor.html')

def prYoshlar(request):
    return render(request, 'rektorat/rektorat/pr-yoshlar.html')

def prOquv(request):
    return render(request, 'rektorat/rektorat/pr-oquv.html')

def prIlmiy(request):
    return render(request, 'rektorat/rektorat/pr-ilmiy.html')

def prMoliya(request):
    return render(request, 'rektorat/rektorat/pr-moliya.html')

def prXalqaro(request):
    return render(request, 'rektorat/rektorat/pr-xalqaro.html')


################################################################################################

def bolimlar(request):
    return render(request, 'rektorat/bolimlar/bolimlar.html')

def pageB1(request):
    return render(request, 'rektorat/bolimlar/page-b1.html')

def pageB2(request):
    return render(request, 'rektorat/bolimlar/page-b2.html')

def pageB3(request):
    return render(request, 'rektorat/bolimlar/page-b3.html')

def pageB4(request):
    return render(request, 'rektorat/bolimlar/page-b4.html')

def pageB5(request):
    return render(request, 'rektorat/bolimlar/page-b5.html')

def pageB6(request):
    return render(request, 'rektorat/bolimlar/page-b6.html')

def pageB7(request):
    return render(request, 'rektorat/bolimlar/page-b7.html')

def pageB8(request):
    return render(request, 'rektorat/bolimlar/page-b8.html')

def pageB9(request):
    return render(request, 'rektorat/bolimlar/page-b9.html')

def pageB10(request):
    return render(request, 'rektorat/bolimlar/page-b10.html')

def pageB11(request):
    return render(request, 'rektorat/bolimlar/page-b11.html')

def pageB12(request):
    return render(request, 'rektorat/bolimlar/page-b12.html')

def pageB13(request):
    return render(request, 'rektorat/bolimlar/page-b13.html')

def pageB14(request):
    return render(request, 'rektorat/bolimlar/page-b14.html')



################################################################################################
################################################################################################

def markazlar(request):
    return render(request, 'rektorat/markazlar/markaz.html')

def pageM1(request):
    return render(request, 'rektorat/markazlar/page-m1.html')


def pageM2(request):
    return render(request, 'rektorat/markazlar/page-m2.html')


def pageM3(request):
    return render(request, 'rektorat/markazlar/page-m3.html')


def pageM4(request):
    return render(request, 'rektorat/markazlar/page-m4.html')


def pageM5(request):
    return render(request, 'rektorat/markazlar/page-m5.html')

def pageM6(request):
    return render(request, 'rektorat/markazlar/page-m6.html')




################################################################################################
################################################################################################

def fakultet(request):
    return render(request, 'rektorat/fakultet/fakultet.html')   

def pageF1(request):
    return render(request, 'rektorat/fakultet/page-f1.html')   

def pageF2(request):
    return render(request, 'rektorat/fakultet/page-f2.html')   

def pageF3(request):
    return render(request, 'rektorat/fakultet/page-f3.html')   

def pageF4(request):
    return render(request, 'rektorat/fakultet/page-f4.html')   

def pageF5(request):
    return render(request, 'rektorat/fakultet/page-f5.html')   

def pageF6(request):
    return render(request, 'rektorat/fakultet/page-f6.html')   


################################################################################################
################################################################################################

def kafedra(request):
    return render(request, 'rektorat/kafedra/kafedra.html')   

def pageK1(request):
    return render(request,'rektorat/kafedra/page-k1.html')

def pageK2(request):
    return render(request,'rektorat/kafedra/page-k2.html')

def pageK3(request):
    return render(request,'rektorat/kafedra/page-k3.html')

def pageK4(request):
    return render(request,'rektorat/kafedra/page-k4.html')

def pageK5(request):
    return render(request,'rektorat/kafedra/page-k5.html')

def pageK6(request):
    return render(request,'rektorat/kafedra/page-k6.html')

def pageK7(request):
    return render(request,'rektorat/kafedra/page-k7.html')

def pageK8(request):
    return render(request,'rektorat/kafedra/page-k8.html')

def pageK9(request):
    return render(request,'rektorat/kafedra/page-k9.html')

def pageK10(request):
    return render(request,'rektorat/kafedra/page-k10.html')

def pageK11(request):
    return render(request,'rektorat/kafedra/page-k11.html')

def pageK12(request):
    return render(request,'rektorat/kafedra/page-k12.html')

def pageK13(request):
    return render(request,'rektorat/kafedra/page-k13.html')

def pageK14(request):
    return render(request,'rektorat/kafedra/page-k14.html')

def pageK15(request):
    return render(request,'rektorat/kafedra/page-k15.html')

def pageK16(request):
    return render(request,'rektorat/kafedra/page-k16.html')

def pageK17(request):
    return render(request,'rektorat/kafedra/page-k17.html')

def pageK18(request):
    return render(request,'rektorat/kafedra/page-k18.html')

def pageK19(request):
    return render(request,'rektorat/kafedra/page-k19.html')

def pageK20(request):
    return render(request,'rektorat/kafedra/page-k20.html')

def pageK21(request):
    return render(request,'rektorat/kafedra/page-k21.html')

def pageK22(request):
    return render(request,'rektorat/kafedra/page-k22.html')

def pageK23(request):
    return render(request,'rektorat/kafedra/page-k23.html')

def pageK24(request):
    return render(request,'rektorat/kafedra/page-k24.html')

def pageK25(request):
    return render(request,'rektorat/kafedra/page-k25.html')

def pageK26(request):
    return render(request,'rektorat/kafedra/page-k26.html')

def pageK27(request):
    return render(request,'rektorat/kafedra/page-k27.html')

def pageK28(request):
    return render(request,'rektorat/kafedra/page-k28.html')


################################################################################################
################################################################################################