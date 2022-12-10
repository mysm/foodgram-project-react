from django.contrib.admin import ModelAdmin, register, site

from .models import MeasurementUnits, Tag

site.site_header = 'Администрирование Foodgram'
EMPTY_VALUE_DISPLAY = 'Значение не указано'


@register(MeasurementUnits)
class IngredientAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
    empy_value_display = EMPTY_VALUE_DISPLAY


@register(Tag)
class TagAdmin(ModelAdmin):
    list_display = ('id', 'name', 'color', 'slug')
    search_fields = ('name', 'slug')
    list_filter = ('name', 'slug')
    empy_value_display = EMPTY_VALUE_DISPLAY
