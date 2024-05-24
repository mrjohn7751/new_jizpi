from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name='index'),
   
    path('yangiliklar/',news,name='news'),
    path('yangiliklar/<int:pk>/',news_detail,name='ArticleNews_details'),
   
    path('elonlar/',elon,name='elon'),
    path('elon/<int:pk>/',elon_detail,name='ArticleElon_detail'),
    
    
    path('institut',institut, name='institut'),
    path('kengashlar',kengash, name='kengash'),
    path('meyoriy-hujjatlar',meyoriyHujjat, name='meyoriy-hujjat'),
    
    path('institut/institut-nizomi',institutPage_1, name='ins-nizomi'),
    path('institut/institut-tarixi',institutPage_2, name='ins-tarixi'),
    path('institut/institut-strukturasi',institutPage_3, name='ins-strukturasi'),
    path('institut/rektor-tabrigi',institutPage_4, name='rektor-tabrigi'),
    path('institut/rekivizitlar',institutPage_5, name='rekivizitlar'),
    path('institut/moddiy-texnik-baza',institutPage_6, name='md-baza'),
    path('institut/sport-inshoatlari',institutPage_7, name='sp-inshoatlari'),
    
    
    path('institut/kengash/OTM-kengash',OTMkengash, name='OTM-kengash'),
    path('institut/kengash/OTM-kengash/kengash-2019-2020',kengash1920, name='kengash1920'),
    path('institut/kengash/OTM-kengash/kengash-2020-2021',kengash2021, name='kengash2021'),
    path('institut/kengash/OTM-kengash/kengash-2021-2022',kengash2122, name='kengash2122'),
    path('institut/kengash/OTM-kengash/kengash-2022-2023',kengash2223, name='kengash2223'),
    path('institut/kengash/OTM-kengash/kengash-2023-2024',kengash2324, name='kengash2324'),
    
    
    path('institut/kengash/Vasiylik',vasiylik, name='vasiylik'),
    path('institut/kengash/Vasiylik/namunaviy-nizom',vp1, name='namunaviy-nizom'),
    path('institut/kengash/Vasiylik/Vasiylik-kengashi-tarkibi',vp2, name='vasiylik-kt'),
    
    
    path('institut/kengash/Yosh-olimalr-kengashi',yoshOlimlar, name='yoshOlimlar'),
    path('institut/kengash/Xotin-Qizlar-kengashi',xotinQizlar, name='xotinQizlar'),
    path('institut/kengash/Ilmiy-kengash',ilmiyKengash, name='ilmiyKengash'),
    
    
    path('institut/meyoriy-hujjatlar/prezident-qarorlari',mhPage1, name='mh-page-1'),
    path('institut/meyoriy-hujjatlar/prezident-farmonlari',mhPage2, name='mh-page-2'),
    path('institut/meyoriy-hujjatlar/vazirlik-buyruqlari',mhPage3, name='mh-page-3'),
    path('institut/meyoriy-hujjatlar/adliya-qarorlari',mhPage4, name='mh-page-4'),
    path('institut/meyoriy-hujjatlar/hukumat-qarorlari',mhPage5, name='mh-page-5'),
    path('institut/meyoriy-hujjatlar/hukumat-dasturi',mhPage6, name='mh-page-6'),
    path('institut/meyoriy-hujjatlar/institut-buyruqlari',mhPage7, name='mh-page-7'),
    path('institut/meyoriy-hujjatlar/klasifikatorlar',mhPage8,name='mh-page-8'),
    
    
    
    path('rektorat',rektorat,name="rektorat"),
    path('rektorat/Rektor',rektor,name="rektor"),
    path('rektorat/Yoshlar-masalalari',prYoshlar,name="prYoshlar"),
    path('rektorat/Oquv-ishlari',prOquv,name="prOquv"),
    path('rektorat/Ilmiy-ishlari',prIlmiy,name="prIlmiy"),
    path('rektorat/Moliyaviy-ishlari',prMoliya,name="prMoliya"),
    path('rektorat/Xalqaro-ishlari',prXalqaro,name="prXalqaro"),
    
    
    
    path('bolimalar',bolimlar,name="bolimlar"),
    
    
    
    path('markazlar',markazlar,name="markazlar"),
    
    
    
]
