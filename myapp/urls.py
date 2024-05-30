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
 
 
    
    path('Xalqaro-faoliyat/', xalqaroFaoliyat, name="xalqaroFaoliyat"),
    path('Xalqaro-faoliyat/pageXF1', pageXF1, name="pageXF1"),
    path('Xalqaro-faoliyat/pageXF2', pageXF2, name="pageXF2"),
    path('Xalqaro-faoliyat/pageXF3', pageXF3, name="pageXF3"),
    path('Xalqaro-faoliyat/pageXF4', pageXF4, name="pageXF4"),
    path('Xalqaro-faoliyat/pageXF5', pageXF5, name="pageXF5"),
    path('Xalqaro-faoliyat/pageXF6', pageXF6, name="pageXF6"),
    
    
    
    path('Moliyaviy-faoliyat/', moliyaviyFaoliyat, name="moliyaviyFaoliyat"),
    path('Moliyaviy-faoliyat/pageMF1', pageMF1, name="pageMF1"),
    path('Moliyaviy-faoliyat/pageMF2', pageMF2, name="pageMF2"),
    path('Moliyaviy-faoliyat/pageMF3', pageMF3, name="pageMF3"),
    path('Moliyaviy-faoliyat/pageMF4', pageMF4, name="pageMF4"),
    path('Moliyaviy-faoliyat/pageMF5', pageMF5, name="pageMF5"),
    path('Moliyaviy-faoliyat/pageMF6', pageMF6, name="pageMF6"),
    path('Moliyaviy-faoliyat/pageMF7', pageMF7, name="pageMF7"),
    
    
    path('callCenter/', callCenter, name="callCenter"),
    path('bakalavr/', bakalavr, name="bakalavr"),
    path('bakalavr/qabul/pageB1', pageB1, name="pageB1"),
    path('bakalavr/qabul/pageB2', pageB2, name="pageB2"),
    path('bakalavr/qabul/pageB3', pageB3, name="pageB3"),
    path('bakalavr/qabul/pageB4', pageB4, name="pageB4"),
    path('bakalavr/qabul/pageB5', pageB5, name="pageB5"),
    path('bakalavr/qabul/pageB6', pageB6, name="pageB6"),
    path('bakalavr/qabul/pageB7', pageB7, name="pageB7"),
    path('bakalavr/qabul/pageB8', pageB8, name="pageB8"),
    
    
    path('magistratura/', magistr, name="magistr"),
    path('magistratura/pageQM1', pageQM1, name="pageQM1"),
    path('magistratura/pageQM2', pageQM2, name="pageQM2"),
    path('magistratura/pageQM3', pageQM3, name="pageQM3"),
    path('magistratura/pageQM4', pageQM4, name="pageQM4"),
    path('magistratura/pageQM5', pageQM5, name="pageQM5"),
    path('magistratura/pageQM6', pageQM6, name="pageQM6"),
    path('magistratura/pageQM7', pageQM7, name="pageQM7"),
    path('magistratura/pageQM8', pageQM8, name="pageQM8"),
    path('magistratura/pageQM9', pageQM9, name="pageQM9"),
    
    
    path('sirtqi-talim', sirtqi, name='sirtqi'),
    path('sirtqi-talim/pageSirtqi1', pageSirtqi1, name='pageSirtqi1'),
    path('sirtqi-talim/pageSirtqi2', pageSirtqi2, name='pageSirtqi2'),
    path('sirtqi-talim/pageSirtqi3', pageSirtqi3, name='pageSirtqi3'),
    path('sirtqi-talim/pageSirtqi4', pageSirtqi4, name='pageSirtqi4'),
    path('sirtqi-talim/pageSirtqi5', pageSirtqi5, name='pageSirtqi5'),
    path('sirtqi-talim/pageSirtqi6', pageSirtqi6, name='pageSirtqi6'),
    path('sirtqi-talim/pageSirtqi7', pageSirtqi7, name='pageSirtqi7'),
    path('sirtqi-talim/pageSirtqi8', pageSirtqi8, name='pageSirtqi8'),
    
    
    path('Xorijiy-Talabalar', xorijiyTalabalar, name='xorijiyTalabalar'),
    path('texnikumlar', texnikum, name='texnikum'),
    
    path('Qo\'shma-Talim-Dasturi', qoshmaTalim, name='qoshmaTalim'),
    path('Qo\'shma-Talim-Dasturi/pageQT1', pageQT1, name='pageQT1'),
    path('Qo\'shma-Talim-Dasturi/pageQT2', pageQT2, name='pageQT2'),
    path('Qo\'shma-Talim-Dasturi/pageQT3', pageQT3, name='pageQT3'),
    path('Qo\'shma-Talim-Dasturi/pageQT4', pageQT4, name='pageQT4'),
    path('Qo\'shma-Talim-Dasturi/pageQT5', pageQT5, name='pageQT5'),
    path('Qo\'shma-Talim-Dasturi/pageQT6', pageQT6, name='pageQT6'),
    path('Qo\'shma-Talim-Dasturi/pageQT7', pageQT7, name='pageQT7'),
    path('Qo\'shma-Talim-Dasturi/pageQT8', pageQT8, name='pageQT8'),
    path('Qo\'shma-Talim-Dasturi/pageQT9', pageQT9, name='pageQT9'),
    path('Qo\'shma-Talim-Dasturi/pageQT10', pageQT10, name='pageQT10'),
    
    
    
    
    path('doktarantura', doktarantura, name='doktarantura'),
    path('doktarantura/pageDOK1', pageDOK1, name='pageDOK1'),
    path('doktarantura/pageDOK2', pageDOK2, name='pageDOK2'),
    path('doktarantura/pageDOK3', pageDOK3, name='pageDOK3'),
    path('doktarantura/pageDOK4', pageDOK4, name='pageDOK4'),
    path('doktarantura/pageDOK5', pageDOK5, name='pageDOK5'),


    path('Ikkinchi-Mutaxasislik', ikkiMutaxasislik, name='ikkiMutaxasislik'),
    path('Ikkinchi-Mutaxasislik/pageIM1', pageIM1, name='pageIM1'),
    path('Ikkinchi-Mutaxasislik/pageIM2', pageIM2, name='pageIM2'),
    path('Ikkinchi-Mutaxasislik/pageIM3', pageIM3, name='pageIM3'),
    path('Ikkinchi-Mutaxasislik/pageIM4', pageIM4, name='pageIM4'),
    path('Ikkinchi-Mutaxasislik/pageIM5', pageIM5, name='pageIM5'),
    path('Ikkinchi-Mutaxasislik/pageIM6', pageIM6, name='pageIM6'),
    path('Ikkinchi-Mutaxasislik/pageIM7', pageIM7, name='pageIM7'),
    path('Ikkinchi-Mutaxasislik/pageIM8', pageIM8, name='pageIM8'),
    path('Ikkinchi-Mutaxasislik/pageIM9', pageIM9, name='pageIM9'),
    path('Ikkinchi-Mutaxasislik/pageIM10', pageIM10, name='pageIM10'),


]
