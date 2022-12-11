from django.contrib.admin import ModelAdmin, register, site, TabularInline
from django.utils.safestring import mark_safe
from django.db.models import Count

from .models import MeasurementUnits, Tag, Ingredient, Recipe, AmountIngredient

site.site_header = "Администрирование Foodgram"
EMPTY_VALUE_DISPLAY = "Значение не указано"


class IngredientInline(TabularInline):
    model = AmountIngredient
    extra = 2


@register(MeasurementUnits)
class IngredientAdmin(ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_filter = ("name",)
    empy_value_display = EMPTY_VALUE_DISPLAY


@register(Tag)
class TagAdmin(ModelAdmin):
    list_display = ("id", "name", "color", "slug")
    search_fields = ("name", "slug")
    list_filter = ("name", "slug")
    empy_value_display = EMPTY_VALUE_DISPLAY


@register(Ingredient)
class IngredientAdmin(ModelAdmin):
    list_display = ("id", "name", "measurement_unit")
    search_fields = ("name",)
    list_filter = ("name",)
    empy_value_display = EMPTY_VALUE_DISPLAY


def favorite_count(obj):
    return obj.obj_count


@register(Recipe)
class RecipeAdmin(ModelAdmin):
    list_display = (
        "id",
        "name",
        "author",
        "text",
        "get_image",
        "pub_date",
    )
    fields = (
        (
            "name",
            "cooking_time",
        ),
        (
            "author",
            "tags",
        ),
        ("text",),
        ("image",),
    )
    search_fields = ("name", "author", "tags")
    list_filter = (
        "name",
        "author__username",
    )
    filter_vertical = ("tags",)

    inlines = (IngredientInline,)
    save_on_top = True
    empty_value_display = EMPTY_VALUE_DISPLAY

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="80" height="30"')

    get_image.short_description = "Изображение"
