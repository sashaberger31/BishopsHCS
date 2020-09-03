from django.contrib import admin

# Register your models here.
from pages.models import WebText, WebSection, WebImg, WebPage, WebInnerLink

admin.site.register(WebText)
admin.site.register(WebSection)
admin.site.register(WebImg)
admin.site.register(WebPage)
admin.site.register(WebInnerLink)
