from django.contrib import admin
from .models import DocumentGroup, Document, AccessKey

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('group', 'imprecise_views')

class AccessKeyAdmin(admin.ModelAdmin):
    list_display = ('group', 'key', 'imprecise_uses')

admin.site.register(Document, DocumentAdmin)
admin.site.register(DocumentGroup)
admin.site.register(AccessKey, AccessKeyAdmin)