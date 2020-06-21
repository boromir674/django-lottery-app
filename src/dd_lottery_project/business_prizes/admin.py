from django.contrib import admin

from .models import *

import logging
logger = logging.getLogger(__name__)


class BusinessAdmin(admin.ModelAdmin):
    model = Business
    list_display = ('name', 'user', 'description', 'email', 'address', 'website', 'receit')

    def receit(self, obj):
        try:
            return obj.receit.width
        except Exception as e:
            return ''


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('name', 'description', 'value', 'business')

 
class ReceitAdmin(admin.ModelAdmin):
    model = Receit
    list_display = ('width', 'cnt', 'pct')

    def width(self, obj):
        return obj.width

    def cnt(self, obj):
        try:
            return Business.objects.filter(receit=obj).count()
        except Exception:
            return 0

    def pct(self, obj):
        return Business.objects.nb_businesses_with_receit()

    # search_fields = ('competition', 'state')


admin.site.register(Business, BusinessAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Receit, ReceitAdmin)
