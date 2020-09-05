from django.contrib import admin

# Register your models here.
from pages.models import WebText, WebSection, WebImg, WebPage, WebInnerLink

class WebSectionItem(admin.ModelAdmin):
    search_fields = ['parent_page__name', 'name', 'parent_section__name']
    autocomplete_fields = ['parent_section']

class WebTextItem(admin.ModelAdmin):
    search_fields = ['parent_page__name', 'name', 'parent_section__name']
    autocomplete_fields = ['parent_section']
    
admin.site.register(WebText, WebTextItem)
admin.site.register(WebSection, WebSectionItem)
admin.site.register(WebImg)
admin.site.register(WebPage)
admin.site.register(WebInnerLink)
