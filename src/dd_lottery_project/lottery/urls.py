from django.contrib import admin as dj_admin
from django.urls import path

from .views.winner import CodeChecker

urlpatterns = [
    path('', CodeChecker.as_view(), name='lottery_index'),
    path('lot_admin/', dj_admin.site.urls, name='lottery_admin'),
]
