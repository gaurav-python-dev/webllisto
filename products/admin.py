from django.contrib import admin
from .models import Product, Category, Tag

#admin header and title
admin.site.site_header = 'Webllisto'
admin.site.site_title = 'Webllisto'
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name','image','description','category',]
    list_filter = ['category']
    search_fields = ['product_name']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class TagAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Tag,TagAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)

