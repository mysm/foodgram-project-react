from django.contrib.admin import ModelAdmin, TabularInline, register, site
from django.db.models import Count
from django.utils.safestring import mark_safe

from .models import (FavoriteRecipe, Ingredient, IngredientAmount, Recipe,
                     ShoppingCart, Subscribe, Tag)

site.site_header = "Администрирование Foodgram"
EMPTY_VALUE_DISPLAY = "Значение не указано"


class IngredientInline(TabularInline):
    model = IngredientAmount
    extra = 2
    autocomplete_fields = ("ingredient",)
    min_num = 1


@register(IngredientAmount)
class IngredientAmount(ModelAdmin):
    list_display = ("id", "recipe", "ingredient", "amount")
    search_fields = ("recipe", "ingredient")
    list_filter = ("id", "recipe", "ingredient")
    empy_value_display = EMPTY_VALUE_DISPLAY


@register(FavoriteRecipe)
class FavoriteAdmin(ModelAdmin):
    list_display = ("id", "user", "favorite_recipe")
    search_fields = ("favorite_recipe",)
    list_filter = ("id", "user", "favorite_recipe")
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


@register(Recipe)
class RecipeAdmin(ModelAdmin):
    list_display = (
        "id",
        "name",
        "author",
        "text",
        "get_image",
        "pub_date",
        "favorite_count",
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
    search_fields = ("name", "author__username", "tags__name")
    list_filter = ("name", "author__username", "tags__name", "pub_date")
    filter_vertical = ("tags",)

    inlines = (IngredientInline,)
    save_on_top = True
    empty_value_display = EMPTY_VALUE_DISPLAY

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="80" height="30"')

    get_image.short_description = "Изображение"

    def favorite_count(self, obj):
        return obj.obj_count

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.annotate(
            obj_count=Count("favorite_recipe", distinct=True),
        )


@register(Subscribe)
class SubscribeAdmin(ModelAdmin):
    list_display = ("id", "author", "user", "created")
    search_fields = ("author", "created")
    list_filter = ("author", "user", "created")
    empy_value_display = EMPTY_VALUE_DISPLAY


@register(ShoppingCart)
class ShoppingCartAdmin(ModelAdmin):
    list_display = ("id", "user", "recipe")
    search_fields = ("user", "recipe")
    list_filter = ("user", "recipe")
    empy_value_display = EMPTY_VALUE_DISPLAY
