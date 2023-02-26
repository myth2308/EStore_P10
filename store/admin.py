from django.contrib import admin
# Tao thu muc tren trang admin
from . import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name'] #tao slug cho sp moi
    ordering = ['name']
    list_display = ['name', 'slug']


@admin.register(models.SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    autocomplete_fields = ['category'] #tao slug cho sp moi
    prepopulated_fields = {
        'slug': ['name'] #tao slug cho sp moi
    }
    list_display = ['name','category_name','image','slug']
    search_fields = ['name'] #tao moi

    def category_name(self, subcategory):
        return subcategory.category.name

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ['subcategory'] # tao moi tim theo ten
    list_display = ['name', 'price', 'viewed_status','subcategory_name']
    list_filter = ['public_day', 'subcategory'] # lọc sản phẩm
    list_editable = ['price'] # chỉnh sửa sản phẩm
    list_per_page = 10 # phân trang
    search_fields = ['name__startswith'] # tìm sản phẩm
    ordering = ['name', 'price']

    def subcategory_name(self, product):
        return product.subcategory.name

    @admin.display(ordering='viewed') #chọn thứ tự < >
    def viewed_status(self, product):
        if product.viewed == 0:
            return 'No'
        return 'Yes'
    
