# -*- coding: utf-8 -*-
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.conf.urls import url
from django.contrib import admin, messages
from django.shortcuts import redirect

from dashboard.models.country import Country
from dashboard.models.janssen_sku import JanssenSKU
from dashboard.models.package import Package, PackageProductRow, WarehousePackageRow
from dashboard.models.product import Product
from dashboard.models.shop import Shop, ShopTrackingCompany
from dashboard.models.subscription_offer import SubscriptionOffer
from dashboard.models.subscription_website import SubscriptionWebsite
from dashboard.models.employee import Employee
from dashboard.models.partner import Partner
from dashboard.models.warehouse import Warehouse, OrderTurnaroundSLA
from dashboard.models.warehouse import WarehouseLocation, WarehouseLocationCode
from dashboard.models.warehouse_exception import WarehouseException
from dashboard.models.order_tag import OrderTagLink  # noqa
from dashboard.models.order_row import OrderRow  # noqa
from dashboard.models.order import Order  # noqa
from dashboard.models.warehouse_response import WarehouseResponse
from dashboard.models.warehouse import Settings
from dashboard.models.shipping_method import ShippingMethod
from rangefilter.filter import DateRangeFilter


class ShopAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(ShopAdmin, self).get_form(request, obj, **kwargs)
        del form.base_fields['modified']
        return form


class PackageProductRowInline(admin.TabularInline):
    model = PackageProductRow


class WarehousePackageRowInline(admin.TabularInline):
    model = WarehousePackageRow


class CountryInline(admin.TabularInline):
    model = Country


class WarehouseLocationCodeInline(admin.TabularInline):
    model = WarehouseLocationCode


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'identifier')

    ordering = ['name']
    inlines = [CountryInline]


class WarehouseLocationAdmin(admin.ModelAdmin):
    list_display = ('warehouse',
                    'name',
                    'shopify_location_id')

    ordering = ['warehouse']
    inlines = [WarehouseLocationCodeInline]



class OrderTurnaroundSLAAdmin(admin.ModelAdmin):
    list_display = ('warehouse',
                    'days_to_ship',)

    ordering = ['warehouse']


def get_columns_to_display(user):

    DEFAULT_COLUMNS = (
        'created',
        'dashboard_id',
        'warehouse',
        'warehouse_order_id',
        'shopify_order_id',
        'status_change',
        'state',
        'refunded',
        'last_name',
        'email',
        'country',
    )

    try:
        if Settings.objects.count():
            settings = Settings.objects.get(user=user)
            return settings.order_columns + ['last_run_status']
    except Exception:
        pass

    return DEFAULT_COLUMNS


class WarehouseResponseAdmin(admin.TabularInline):
    model = WarehouseResponse

    ordering = ['-created']

    fields = ('created', 'request_type', 'request',
              'response', 'message', 'success')

    readonly_fields = [
        'created',
        'request_type',
        'request',
        'response',
        'success',
        'message'
    ]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class OrderLogsAdmin(admin.ModelAdmin):

    fields = (
        'dashboard_id',
        'warehouse',
        'warehouse_order_id',
        'shopify_order_id',
        'created',
        'warehouse_status_change_date',
        'state',
        'refunded',
        'payment_date',
        'last_name',
        'email',
        'country',
        # Temporary add tracking-related fields to test
        # Dashboard -> Shopify integration
        'track_trace',
        'shipping_method',
        'sent_tracking_to_shop_state',
    )

    list_filter = (
        'warehouse',
        ('created', DateRangeFilter),
        ('warehouse_status_change_date', DateRangeFilter),
    )

    search_fields = [
        'id',
        'shopify_order_id',
        'warehouse_order_id',
        'customer_details__shipping_last_name',
        'customer_details__email',
        'packages__identifier',
        'packages__warehouse_packages__warehouse_sku'
    ]

    readonly_fields = [
        'dashboard_id',
        'warehouse',
        'shopify_order_id',
        'created',
        'warehouse_status_change_date',
        'state',
        'refunded',
        'last_name',
        'email',
        'country',
    ]

    inlines = [
        WarehouseResponseAdmin,
    ]

    def get_form(self, request, obj=None, **kwargs):
        form = super(OrderLogsAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['warehouse_order_id'].required = False
        form.base_fields['track_trace'].required = False
        form.base_fields['shipping_method'].required = False
        form.base_fields['payment_date'].required = False
        return form

    def changelist_view(self, request, extra_context=None):
        self.list_display = get_columns_to_display(request.user)
        return super(OrderLogsAdmin, self).changelist_view(request, extra_context)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        # Disable delete
        actions = super(OrderLogsAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def dashboard_id(self, obj):
        return '<a href="/orders/view/{order_id}">{order_id}</a>'.format(
            order_id=obj.id
        )
    dashboard_id.allow_tags = True

    def last_run_status(self, obj):
        result = WarehouseResponse.objects.filter(
            order=obj).order_by('-created')
        if result:
            response = result[0]
            if response.success:
                return 'SUCCESS'
            else:
                return 'FAIL'
        return '-'

    def status_change(self, obj):
        return obj.warehouse_status_change_date

    def refunded(self, obj):
        if obj.refunded_date:
            return 'Yes'
        return 'No'

    def last_name(self, obj):
        if obj.customer_details:
            return obj.customer_details.shipping_last_name
        return ''

    def email(self, obj):
        if obj.customer_details:
            return obj.customer_details.email
        return ''

    def country(self, obj):
        if obj.customer_details:
            return obj.customer_details.shipping_country
        return ''


class SettingsAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        self.exclude = ('user',)
        form = super(SettingsAdmin, self).get_form(
            request,
            obj,
            **kwargs
        )
        return form

    def get_queryset(self, request):
        qs = super(SettingsAdmin, self).get_queryset(request)
        return qs.filter(user=request.user)

    def has_add_permission(self, request):
        if Settings.objects.filter(user=request.user).count() > 0:
            return False
        return True

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


class JanssenSKUInline(admin.TabularInline):
    model = JanssenSKU

class WarehouseExceptionAdmin(admin.ModelAdmin):
    list_display = ('package', 'shipping_countries','warehouse')
    ordering = ['package']
    def shipping_countries(self, obj):
        return ",\n".join([country.code for country in obj.countries.all()])


###########
def make_inactive(modeladmin, request, queryset):
    queryset.update(is_enabled=0)


make_inactive.short_description = "Mark product/package as inactive"


def make_active(modeladmin, request, queryset):
    queryset.update(is_enabled=1)


make_active.short_description = "Mark product/package as active"

class PackageAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'identifier',
                    'price',
                    'is_subscription',
                    'is_enabled',)
    list_filter = ('is_enabled',)
    ordering = ['name']
    actions = [make_inactive, make_active]
    inlines = [
        PackageProductRowInline,
        WarehousePackageRowInline,
        JanssenSKUInline
    ]

    def janssen_skus(self, package):
        skus = ["{}x {}".format(sku.cnt, str(sku))
                for sku in package.janssensku_set.all()]
        return '<br/>'.join(skus)

    def fleshlight_products(self, package):
        products = []
        for row in package.packageproductrow_set.all():
            product_str = "{}x {} ({})".\
                format(row.cnt,
                       str(row.product),
                       row.product.fleshlight_id)
            products.append(product_str)
        return '<br/>'.join(products)

    fleshlight_products.allow_tags = True
    janssen_skus.allow_tags = True


class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'commission',
                    'country',
                    'user')


class ShopTrackingCompanyAdmin(admin.ModelAdmin):
    list_display = (
        'warehouse',
        'shop',
        'shipping_method',
        'tracking_company'
    )


class ProductAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ('name',
                    'is_enabled',)
    list_filter = ('is_enabled',)
    actions = [make_inactive, make_active]


class JanssenSKUAdmin(admin.ModelAdmin):
    list_display = ('sku',
                    'product')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'otp_enabled')
    list_display_links = ('user',)
    list_filter = ('otp_enabled',)
    ordering = ['user']


class MyUserAdmin(UserAdmin):

    def __init__(self, *args, **kwargs):
        super(UserAdmin, self).__init__(*args, **kwargs)
        UserAdmin.list_display = list(UserAdmin.list_display) + ['otp_enabled']

    def otp_enabled(self, obj):
        employee = Employee.objects.get(user=obj)
        return employee.otp_enabled


# Register your models here.
admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Shop)
admin.site.register(ShippingMethod)
admin.site.register(Package, PackageAdmin)
admin.site.register(SubscriptionOffer)
admin.site.register(SubscriptionWebsite)
admin.site.register(PackageProductRow)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(ShopTrackingCompany, ShopTrackingCompanyAdmin)

admin.site.register(JanssenSKU, JanssenSKUAdmin)
admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(WarehouseLocation, WarehouseLocationAdmin)
admin.site.register(WarehouseException, WarehouseExceptionAdmin)
admin.site.register(OrderTurnaroundSLA, OrderTurnaroundSLAAdmin)

admin.site.register(Order, OrderLogsAdmin)
admin.site.register(Settings, SettingsAdmin)

admin.site.site_header = 'Kiiroo Administration'
admin.site.index_title = 'Kiiroo Administration'
admin.site.site_title = 'Kiiroo Administration'
