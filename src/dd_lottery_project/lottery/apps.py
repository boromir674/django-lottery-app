from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


class LotteryConfig(AppConfig):
    name = 'lottery'


class MyAdminConfig(AdminConfig):
    name = 'lottery_admin'
    # default_site = 'myproject.admin.MyAdminSite'