from django.contrib import admin
from .models import Antiquity, Category, Period


class AntiquityAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'name',
        'date',
        'period',
        'culture',
        'value',
        'image',
    )

    ordering = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )


class PeriodAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


admin.site.register(Antiquity, AntiquityAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Period, PeriodAdmin)
