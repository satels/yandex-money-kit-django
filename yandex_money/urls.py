# -*- coding: utf-8 -*-

try:
    from django.conf.urls import url
except ImportError:
    from django.urls import re_path as url
from .views import NoticeFormView
from .views import CheckOrderFormView


urlpatterns = [
    url(r'^check/$', CheckOrderFormView.as_view(), name='yandex_money_check'),
    url(r'^aviso/$', NoticeFormView.as_view(), name='yandex_money_notice'),
]
