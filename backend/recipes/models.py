from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

MAX_LEN_RECIPES = 255

models.CharField.register_lookup(models.functions.Length)

User = get_user_model()


class MeasurementUnits(models.Model):
    """Единицы измерения."""

    name = models.CharField(
        verbose_name="Единица измерения",
        max_length=MAX_LEN_RECIPES,
        unique=True,
    )

    class Meta:
        verbose_name = "Единица измерения"
        verbose_name_plural = "Единицы измерения"
        ordering = ("name",)

    def __str__(self):
        return self.name


class Tag(models.Model):
    """Теги."""

    BLUE = "#0000FF"
    ORANGE = "#FFA500"
    GREEN = "#008000"
    PURPLE = "#800080"
    YELLOW = "#FFFF00"
    RED = "#FF0000"

    COLOR_CHOICES = [
        (BLUE, "Синий"),
        (ORANGE, "Оранжевый"),
        (GREEN, "Зеленый"),
        (PURPLE, "Фиолетовый"),
        (YELLOW, "Желтый"),
        (RED, "Красный"),
    ]

    name = models.CharField(
        verbose_name="Название тега",
        max_length=MAX_LEN_RECIPES,
        unique=True,
    )
    color = models.CharField(
        verbose_name="Цветовой HEX-код",
        choices=COLOR_CHOICES,
        max_length=7,
        default=GREEN,
        null=True,
        blank=True,
        unique=True,
    )
    slug = models.SlugField(
        "Slug тега",
        max_length=MAX_LEN_RECIPES,
        unique=True,
    )

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        ordering = ("name",)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """ингредиенты."""

    name = models.CharField(
        verbose_name="Название ингредиента",
        max_length=MAX_LEN_RECIPES,
    )
    measurement_unit = models.ForeignKey(
        verbose_name="Единица измерения",
        related_name="measurement_units",
        to=MeasurementUnits,
        on_delete=models.RESTRICT,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=("name", "measurement_unit"), name="unique_name_measurement"
            )
        ]
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"
        ordering = ("id",)

    def __str__(self):
        return f"{self.name} ({self.measurement_unit})"


class Recipe(models.Model):
    """Рецепты"""

    name = models.CharField(
        verbose_name="Название блюда",
        max_length=MAX_LEN_RECIPES,
    )
    author = models.ForeignKey(
        verbose_name="Автор рецепта",
        related_name="recipes",
        to=User,
        on_delete=models.CASCADE,
    )
    favorite = models.ManyToManyField(
        verbose_name="Понравившиеся рецепты",
        related_name="favorites",
        to=User,
    )
    tags = models.ManyToManyField(
        verbose_name="Тег",
        related_name="recipes",
        to="Tag",
    )
    ingredients = models.ManyToManyField(
        verbose_name="Ингредиенты блюда",
        related_name="recipes",
        to=Ingredient,
        through="recipes.AmountIngredient",
    )
    cart = models.ManyToManyField(
        verbose_name="Список покупок",
        related_name="carts",
        to=User,
    )
    pub_date = models.DateTimeField(
        verbose_name="Дата публикации",
        auto_now_add=True,
    )
    image = models.ImageField(
        verbose_name="Изображение блюда",
        upload_to="recipe_images/",
    )
    text = models.TextField(
        verbose_name="Описание блюда",
        max_length=MAX_LEN_RECIPES,
    )
    cooking_time = models.PositiveSmallIntegerField(
        verbose_name="Время приготовления",
        default=0,
        validators=(MinValueValidator(1, "Минимум одна минута!"),),
    )

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"
        ordering = ("-pub_date",)
        constraints = (
            models.UniqueConstraint(
                fields=("name", "author"), name="unique_for_author"
            ),
            models.CheckConstraint(
                check=models.Q(name__length__gt=0),
                name="name_empty",
            ),
        )

    def __str__(self):
        return f"Автор: {self.author.username} рецепт: {self.name}"


class AmountIngredient(models.Model):
    """Количество ингредиентов в блюде."""

    recipe = models.ForeignKey(
        verbose_name="В каких рецептах",
        related_name="ingredient",
        to=Recipe,
        on_delete=models.CASCADE,
    )
    ingredients = models.ForeignKey(
        verbose_name="Связанные ингредиенты",
        related_name="recipe",
        to=Ingredient,
        on_delete=models.CASCADE,
    )
    amount = models.PositiveSmallIntegerField(
        verbose_name="Количество",
        default=0,
        validators=(
            MinValueValidator(1, "Нужно хоть какое-то количество."),
            MaxValueValidator(10000, "Слишком много!"),
        ),
    )

    class Meta:
        verbose_name = "ингредиент"
        verbose_name_plural = "Количество ингредиентов"
        ordering = ("recipe",)
        constraints = (
            models.UniqueConstraint(
                fields=(
                    "recipe",
                    "ingredients",
                ),
                name="unique_recipe_ingredients",
            ),
        )

    def __str__(self) -> str:
        return f"{self.amount} {self.ingredients}"
