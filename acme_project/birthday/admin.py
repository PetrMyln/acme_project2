from django.contrib import admin

from .models import Birthday, Tag

admin.site.empty_value_display = 'Не задано'


class BirthdayAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'birthday',
    )


class TagAdmin(admin.ModelAdmin):
    pass




admin.site.register(Birthday, BirthdayAdmin)
