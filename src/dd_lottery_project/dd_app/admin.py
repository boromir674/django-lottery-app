from django.contrib import admin
from .models import DdUser
from business_prizes.models import Business


class DdUserAdmin(admin.ModelAdmin):
    model = DdUser
    list_display = ('username', 'business', 'is_staff', 'is_superuser', 'first_name', 'last_name')

    def business(self, obj):
        try:
            return Business.objects.get(user=obj).name
        except Business.DoesNotExist:
            return '-'

admin.site.register(DdUser, DdUserAdmin)
