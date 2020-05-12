from django.contrib.admin.apps import AdminConfig

class MyAdminConfig(AdminConfig):
    default_site = 'dd_lottery_project.admin.MyAdminSite'
