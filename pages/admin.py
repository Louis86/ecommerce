from django.contrib import admin

# Register your models here for admin
from .models import Pages


class PageAdmin(admin.ModelAdmin):
    list_display = ('title','update_date')
    ordering = ('title',)
    search_fields = ('title',)

admin.site.register(Pages,PageAdmin)
