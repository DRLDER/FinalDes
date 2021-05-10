from django.contrib import admin
from django.urls import path, include
from DJ_App.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('testNamePass/', testNameandPass),
    path('info/', showInfo),
    path('memInfoList/', textMemInfo),
    path('ECOOList/', ECOOFormUpdate),
    path('ECOIList/', ECOIFormUpdate),
    path('getECOIO/', ECOIOListUpdate),
    path('ProductionInfoUpdate/', PDInfoUpdate),
    path('PDFormUpdate/', PDFormUpdate),
    path('InfoUpdate/', InfoUpdate),
    path('SureInfoDataUpdate/', SureInfoDataUpdate),
    path('showMeNewInfo/', showmenewInfo),
    path('getAuthority/', getAuthority),
    path('getFutureInfo/', getFutureInfo),
]
