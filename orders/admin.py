from django.contrib import admin
from .models import Order, OrderItem, MyImage, Contact
from django.utils.html import format_html


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'pincode',
                    'created_at', 'product_title', 'product_price']
    list_filter = ['created_at']
    search_fields = ['name', 'phone', 'pincode', 'items__product_title']
    inlines = [OrderItemInline]

    def product_title(self, obj):
        return ', '.join([item.product_title for item in obj.items.all()])

    def product_price(self, obj):
        return ', '.join([str(item.product_price) for item in obj.items.all()])

    product_title.short_description = 'Product Title'
    product_price.short_description = 'Product Price'


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product_title', 'product_price']

    def product_title(self, obj):
        return obj.product.title

    def product_price(self, obj):
        return obj.product.sales_price

    product_title.short_description = 'Product Title'
    product_price.short_description = 'Product Price'


@admin.register(MyImage)
class MyImage(admin.ModelAdmin):
    list_display = ['image']

    def image_tag(self, obj):
        return format_html('<img src="{}" width="100" height="100" />'.format(obj.image.url))

    image_tag.short_description = 'Image'


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'place',  'phone', 'pincode', 'message']
