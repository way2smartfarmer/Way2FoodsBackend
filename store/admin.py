from django.contrib import admin, messages
from . import models
from django import forms
from django.db.models.query import QuerySet
from django.db.models import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse
from .models import ProductImage, Product, MetaLink, CategoryLevelOne, ProductSpecification, ProductHighlight
from .models import CategoryLevelOne,  Product, Banner, Sample


# class InventoryFilter(admin.SimpleListFilter):
#     title = 'sales_price'
#     parameter_name = 'sales_price'

#     def lookups(self, request, model_admin):
#         return [
#             ('<10', 'Low')
#         ]

#     def queryset(self, request, queryset: QuerySet):
#         if self.value() == '<10':
#             return queryset.filter(inventory__lt=10)


# class ProductImageInline(admin.TabularInline):
#     model = ProductImage
#     readonly_fields = ['thumbnail']

#     def thumbnail(self, instance):
#         if instance.image.name != '':
#             return format_html(f'<img src="{instance.image.url}" class="thumbnail"/>')
#         return ''


# class ProductSpecificationInline(admin.TabularInline):
#     model = ProductSpecification
#     extra = 1
#     fields = ('key', 'value')


# class ProductHighlightInline(admin.TabularInline):
#     model = ProductHighlight
#     extra = 1
#     fields = ('highlight')


# class MetaLink(admin.TabularInline):
#     model = MetaLink
#     fields = ('external_link')


# class ProductAdminForm(forms.ModelForm):
#     category_level_one = forms.ModelChoiceField(
#         queryset=CategoryLevelOne.objects.all(),
#         empty_label="Select Category Level One"
#     )

#     class Meta:
#         model = Product
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         if self.instance.pk:
#             # set the initial values of the category fields
#             self.initial['category_level_one'] = self.instance.category_level_one


# @admin.register(models.Product)
# class ProductAdmin(admin.ModelAdmin):
#     form = ProductAdminForm
#     autocomplete_fields = ['collection']
#     search_fields = ['title']
#     prepopulated_fields = {
#         'slug': ['title']
#     }
#     # exclude = ['promotions']

#     actions = ['clear_sales_price']
#     inlines = [ProductSpecificationInline, ProductHighlightInline]
#     list_display = ['title', 'mrp_price',
#                     'sales_price', 'unit', 'collection']
#     list_editable = ['mrp_price']
#     list_filter = ['collection', 'last_update', 'category_level_one',
#                    InventoryFilter]
#     list_per_page = 10
#     list_select_related = ['collection', 'category_level_one',
#                            ]

#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
#         category_level_one_id = request.GET.get('category_level_one')

#         if category_level_one_id:
#             qs = qs.filter(category_level_one_id=category_level_one_id)

#         return qs


# def collection_title(self, product):
#     return product.collection.title


# @admin.display(ordering='mrp_price')
# def inventory_status(self, product):
#     if product.mrp_price < 10:
#         return 'Low'
#     return 'Ok'


# @admin.action(description='Clear mrp_price')
# def clear_mrp_price(self, request, queryset):
#     updated_count = queryset.update(inventory=0)
#     self.message_user(
#         request,
#         f'{updated_count} products were succesfully updated.',
#         messages.ERROR
#     )


# class Media:
#     css = {
#         'all': ['store/styles.css']
#     }


# @admin.register(ProductSpecification)
# class ProductSpecificationAdmin(admin.ModelAdmin):
#     pass


# @admin.register(ProductHighlight)
# class ProductHighlightAdmin(admin.ModelAdmin):
#     pass


# @admin.register(models.Collection)
# class CollectionAdmin(admin.ModelAdmin):
#     autocomplete_fields = ['featured_product']
#     list_display = ['title', 'products_count']
#     search_fields = ['title_istartswith']

#     @admin.display(ordering='products_count')
#     def products_count(self, collection):
#         url = (reverse('admin:store_product_changelist')
#                + '?'
#                + urlencode({
#                    'collection_id': str(collection.id)
#                }))
#         return format_html('<a href="{}">{} Products</a>', url,
#                            collection.products_count)

#     def get_queryset(self, request):
#         return super().get_queryset(request).annotate(
#             products_count=Count('products')
#         )


# @admin.register(models.Customer)
# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ['first_name', 'last_name', 'membership', 'orders']
#     list_editable = ['membership']
#     list_per_page = 10
#     list_select_related = ['user']
#     ordering = ['user__first_name', 'user__last_name']
#     search_fields = ['first_name__istartswith', 'last_name__startswith']

#     @admin.display(ordering='orders_count')
#     def orders(self, customer):
#         url = (
#             reverse('admin:store_order_changelist')
#             + '?'
#             + urlencode({
#                 'customer__id': str(customer.id)
#             }))
#         return format_html('<a href="{}">{} Orders</a>', url, customer.orders_count)

#     def get_queryset(self, request):
#         return super().get_queryset(request).annotate(
#             orders_count=Count('order')
#         )


# @admin.register(models.Subscriber)
# class SubscriberAdmin(admin.ModelAdmin):
#     autocomplete_fields = ['product']
#     list_display = ['email', 'product', 'created_at']
#     search_fields = ['email']


# @admin.register(models.Shipping)
# class ShippingAdmin(admin.ModelAdmin):
#     list_display = ['name', 'address', 'city', 'phone', 'pincode']
#     search_fields = ['name']


# @admin.register(models.Banner)
# class BannerAdmin(admin.ModelAdmin):
#     list_display = ['name']


# @admin.register(models.MetaLink)
# class MetaLinkAdmin(admin.ModelAdmin):
#     list_display = ['external_link']


# @admin.register(models.Sample)
# class MetaLinkAdmin(admin.ModelAdmin):
#     list_display = ['name']
