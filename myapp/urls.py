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
    path('bolimalar/pageB1',pageB1,name="pageB1"),
    path('bolimalar/pageB2',pageB2,name="pageB2"),
    path('bolimalar/pageB3',pageB3,name="pageB3"),
    path('bolimalar/pageB4',pageB4,name="pageB4"),
    path('bolimalar/pageB5',pageB5,name="pageB5"),
    path('bolimalar/pageB6',pageB6,name="pageB6"),
    path('bolimalar/pageB7',pageB7,name="pageB7"),
    path('bolimalar/pageB8',pageB8,name="pageB8"),
    path('bolimalar/pageB9',pageB9,name="pageB9"),
    path('bolimalar/pageB10',pageB10,name="pageB10"),
    path('bolimalar/pageB11',pageB11,name="pageB11"),
    path('bolimalar/pageB12',pageB12,name="pageB12"),
    path('bolimalar/pageB13',pageB13,name="pageB13"),
    path('bolimalar/pageB14',pageB14,name="pageB14"),

    
    
    
    path('markazlar',markazlar,name="markazlar"),
    path('markazlar/pageM1',pageM1,name="pageM1"),
    path('markazlar/pageM2',pageM2,name="pageM2"),
    path('markazlar/pageM3',pageM3,name="pageM3"),
    path('markazlar/pageM4',pageM4,name="pageM4"),
    path('markazlar/pageM5',pageM5,name="pageM5"),
    path('markazlar/pageM6',pageM6,name="pageM6"),
    
    
    
    path('fakultetlar',fakultet,name="fakultet"),
    path('fakultetlar/pageF1',pageF1,name="pageF1"),
    path('fakultetlar/pageF2',pageF2,name="pageF2"),
    path('fakultetlar/pageF3',pageF3,name="pageF3"),
    path('fakultetlar/pageF4',pageF4,name="pageF4"),
    path('fakultetlar/pageF5',pageF5,name="pageF5"),
    path('fakultetlar/pageF6',pageF6,name="pageF6"),
    
    
    
    path('kafedralar',kafedra,name="kafedra"),
    path('kafedralar/pageK1',pageK1,name="pageK1"),
    path('kafedralar/pageK2',pageK2,name="pageK2"),
    path('kafedralar/pageK3',pageK3,name="pageK3"),
    path('kafedralar/pageK4',pageK4,name="pageK4"),
    path('kafedralar/pageK5',pageK5,name="pageK5"),
    path('kafedralar/pageK6',pageK6,name="pageK6"),
    path('kafedralar/pageK7',pageK7,name="pageK7"),
    path('kafedralar/pageK8',pageK8,name="pageK8"),
    path('kafedralar/pageK9',pageK9,name="pageK9"),
    path('kafedralar/pageK10',pageK10,name="pageK10"),
    path('kafedralar/pageK11',pageK11,name="pageK11"),
    path('kafedralar/pageK12',pageK12,name="pageK12"),
    path('kafedralar/pageK13',pageK13,name="pageK13"),
    path('kafedralar/pageK14',pageK14,name="pageK14"),
    path('kafedralar/pageK15',pageK15,name="pageK15"),
    path('kafedralar/pageK16',pageK16,name="pageK16"),
    path('kafedralar/pageK17',pageK17,name="pageK17"),
    path('kafedralar/pageK18',pageK18,name="pageK18"),
    path('kafedralar/pageK19',pageK19,name="pageK19"),
    path('kafedralar/pageK20',pageK20,name="pageK20"),
    path('kafedralar/pageK21',pageK21,name="pageK21"),
    path('kafedralar/pageK22',pageK22,name="pageK22"),
    path('kafedralar/pageK23',pageK23,name="pageK23"),
    path('kafedralar/pageK24',pageK24,name="pageK24"),
    path('kafedralar/pageK25',pageK25,name="pageK25"),
    path('kafedralar/pageK26',pageK26,name="pageK26"),
    path('kafedralar/pageK27',pageK27,name="pageK27"),
    path('kafedralar/pageK28',pageK28,name="pageK28"),
    
    
    
    path('ilmiy-faoliyat/', ilmiyFaoliyat, name="ilmiyFaoliyat"),
    path('ilmiy-faoliyat/pageIF1', pageIF1, name="pageIF1"),
    path('ilmiy-faoliyat/pageIF2', pageIF2, name="pageIF2"),
    path('ilmiy-faoliyat/pageIF3', pageIF3, name="pageIF3"),
    path('ilmiy-faoliyat/pageIF4', pageIF4, name="pageIF4"),
    path('ilmiy-faoliyat/pageIF5', pageIF5, name="pageIF5"),
    path('ilmiy-faoliyat/pageIF6', pageIF6, name="pageIF6"),
    path('ilmiy-faoliyat/pageIF7', pageIF7, name="pageIF7"),
    path('ilmiy-faoliyat/pageIF8', pageIF8, name="pageIF8"),
    path('ilmiy-faoliyat/pageIF9', pageIF9, name="pageIF9"),
    path('ilmiy-faoliyat/pageIF10', pageIF10, name="pageIF10"),
    path('ilmiy-faoliyat/pageIF11', pageIF11, name="pageIF11"),
    path('ilmiy-faoliyat/pageIF12', pageIF12, name="pageIF12"),
    path('ilmiy-faoliyat/pageIF13', pageIF13, name="pageIF13"),
    path('ilmiy-faoliyat/pageIF14', pageIF14, name="pageIF14"),
    path('ilmiy-faoliyat/pageIF15', pageIF15, name="pageIF15"),
    path('ilmiy-faoliyat/pageIF16', pageIF16, name="pageIF16"),
    path('ilmiy-faoliyat/pageIF17', pageIF17, name="pageIF17"),
 
 
 
    path('oquv-faoliyat/', oquvFaoliyat, name="oquvFaoliyat"),
    path('oquv-faoliyat/pageOF1', pageOF1, name="pageOF1"),
    path('oquv-faoliyat/pageOF2', pageOF2, name="pageOF2"),
    path('oquv-faoliyat/pageOF3', pageOF3, name="pageOF3"),
    path('oquv-faoliyat/pageOF4', pageOF4, name="pageOF4"),
    path('oquv-faoliyat/pageOF5', pageOF5, name="pageOF5"),
 
 
    
]
