from django.contrib import admin

from orders.models import Order, OrderProduct


class OrderProductsInline(admin.TabularInline):
    model = OrderProduct
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderProductsInline]


admin.site.register(Order, OrderAdmin)