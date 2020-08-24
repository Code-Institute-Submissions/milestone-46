from django.contrib import admin
from .models import Latest_option


class Latest_optionAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'value',
        'image',
        'antiquity_id',
    )

    ordering = ('name',)


admin.site.register(Latest_option, Latest_optionAdmin)
