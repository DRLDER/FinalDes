from django.conf.urls import url, static
from django.contrib import admin
from django.contrib.staticfiles.views import serve

from django.urls import path, include
from DJ_App.views import *
from FinalDes import settings
from FinalDes.settings import STATIC_ROOT

urlpatterns = [
    url(r'^static/(?P<path>.*)$', static.serve,
        {'document_root': settings.STATIC_ROOT}, name='static'),
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
