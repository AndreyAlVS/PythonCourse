from django.contrib import admin
from .models import Order, OrderItem, Client, Product


@admin.action(description="address reset")
def address_reset(modeladmin, request, queryset):
    queryset.update(address='')


@admin.action(description="quantity_reset")
def quantity_reset(modeladmin, request, queryset):
    queryset.update(quantity=0)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['pk','name', 'email']
    ordering = ['name']
    list_per_page = 10
    search_fields = ['name']
    actions = [address_reset]
    fieldsets = [
        (
            'Client',
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Client data',
                'fields': ['email', 'phone_number', 'address'],
            },
        ),
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['prod_name', 'add_date']
    ordering = ['prod_name']
    list_per_page = 10
    search_fields = ['prod_name']
    actions = [quantity_reset]
    fieldsets = [
        (
            'Product',
            {
                'classes': ['wide'],
                'fields': ['prod_name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Product description',
                'fields': ['description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'quantity'],
            }
        ),
        (
            'Прочее',
            {
                'fields': ['photo'],
            }
        ),
    ]


admin.site.register(Order)
admin.site.register(OrderItem)
# admin.site.register(Client, ClientAdmin)
# admin.site.register(Product)
