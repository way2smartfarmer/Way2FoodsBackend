from django.contrib import admin
from .models import Category, MajorVegetables, RegularVegetables, OtherVegetables, LeafyVegetables, ExoticFruits, ExoticVegetables, MajorFruits, Grains, Spices, Oils, SpecialPackages, MetaLink, Banner


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ['title', 'image', 'description', 'slug',
                    'meta_title', 'meta_description', 'meta_keywords']
    prepopulated_fields = {'slug': ['title']}


class MajorVegAdmin(admin.ModelAdmin):
    model = MajorVegetables
    list_display = ['title', 'image', 'slug', 'price', 'unit',
                    'available', 'meta_title', 'meta_description', 'meta_keywords']
    prepopulated_fields = {'slug': ['title']}
    list_editable = ['price', 'available', 'unit']


class RegularVegAdmin(admin.ModelAdmin):
    model = MajorVegetables
    list_display = ['title', 'image', 'slug', 'price', 'unit',
                    'available', 'meta_title', 'meta_description', 'meta_keywords']
    prepopulated_fields = {'slug': ['title']}
    list_editable = ['price', 'available', 'unit']


class OtherVegAdmin(admin.ModelAdmin):
    model = OtherVegetables
    list_display = ['title', 'image', 'slug', 'price', 'unit',
                    'available', 'meta_title', 'meta_description', 'meta_keywords']
    prepopulated_fields = {'slug': ['title']}
    list_editable = ['price', 'available', 'unit']


class LeafyVegAdmin(admin.ModelAdmin):
    model = LeafyVegetables
    list_display = ['title', 'image', 'slug', 'price', 'unit',
                    'available', 'meta_title', 'meta_description', 'meta_keywords']
    prepopulated_fields = {'slug': ['title']}
    list_editable = ['price', 'available', 'unit']


class ExoticVegAdmin(admin.ModelAdmin):
    model = ExoticVegetables
    list_display = ['title', 'image', 'slug', 'price', 'unit',
                    'available', 'meta_title', 'meta_description', 'meta_keywords']
    prepopulated_fields = {'slug': ['title']}
    list_editable = ['price', 'available', 'unit']


class MajorFruitsAdmin(admin.ModelAdmin):
    model = MajorFruits
    list_display = ['title', 'image', 'slug', 'price', 'unit',
                    'available', 'meta_title', 'meta_description', 'meta_keywords']
    prepopulated_fields = {'slug': ['title']}
    list_editable = ['price', 'available', 'unit']


class ExoticFruitsAdmin(admin.ModelAdmin):
    model = ExoticFruits
    list_display = ['title', 'image', 'slug', 'price', 'unit',
                    'available', 'meta_title', 'meta_description', 'meta_keywords']
    prepopulated_fields = {'slug': ['title']}
    list_editable = ['price', 'available', 'unit']


class GrainsAdmin(admin.ModelAdmin):
    model = Grains
    list_display = ['title', 'image', 'slug', 'price', 'unit',
                    'available', 'meta_title', 'meta_description', 'meta_keywords']
    prepopulated_fields = {'slug': ['title']}
    list_editable = ['price', 'available', 'unit']


class SpicesAdmin(admin.ModelAdmin):
    model = Spices
    list_display = ['title', 'image', 'slug', 'price', 'unit',
                    'available', 'meta_title', 'meta_description', 'meta_keywords']
    prepopulated_fields = {'slug': ['title']}
    list_editable = ['price', 'available', 'unit']


class OilsAdmin(admin.ModelAdmin):
    model = Oils
    list_display = ['title', 'image', 'slug', 'price', 'unit',
                    'available', 'meta_title', 'meta_description', 'meta_keywords']
    prepopulated_fields = {'slug': ['title']}
    list_editable = ['price', 'available', 'unit']


class SpecialPackagesAdmin(admin.ModelAdmin):
    model = SpecialPackages
    list_display = ['title', 'image', 'slug', 'price', 'unit',
                    'available', 'meta_title', 'meta_description', 'meta_keywords']
    prepopulated_fields = {'slug': ['title']}
    list_editable = ['price', 'available', 'unit']


admin.site.register(Category, CategoryAdmin)
admin.site.register(MajorVegetables, MajorVegAdmin)
admin.site.register(RegularVegetables, RegularVegAdmin)
admin.site.register(OtherVegetables, OtherVegAdmin)
admin.site.register(LeafyVegetables, LeafyVegAdmin)
admin.site.register(ExoticFruits, ExoticFruitsAdmin)
admin.site.register(ExoticVegetables, ExoticVegAdmin)
admin.site.register(MajorFruits, MajorFruitsAdmin)
admin.site.register(Grains, GrainsAdmin)

admin.site.register(Spices, SpicesAdmin)
admin.site.register(Oils, OilsAdmin)
admin.site.register(SpecialPackages, SpecialPackagesAdmin)
admin.site.register(MetaLink)
admin.site.register(Banner)
