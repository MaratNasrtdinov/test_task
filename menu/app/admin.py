from django.contrib import admin
from app.models import Elements


@admin.register(Elements)
class ElementsAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    fields = ('id', 'name', 'parent', 'url')
    readonly_fields = ('id',)
