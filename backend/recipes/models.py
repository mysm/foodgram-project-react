from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

MAX_LEN_RECIPES = 255

User = get_user_model()


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
    name = models.CharField(
        "Название ингредиента",
        max_length=MAX_LEN_RECIPES,
    )
    measurement_unit = models.CharField("Единицы измерения", max_length=MAX_LEN_RECIPES)

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
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Автор рецепта",
        related_name="recipe",
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        verbose_name="Ингредиенты",
        through="IngredientAmount",
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name="Тег",
        related_name="recipes",
    )
    image = models.ImageField(
        "Изображение рецепта",
        upload_to="recipes/images",
    )
    name = models.CharField(
        "Название рецепта",
        max_length=MAX_LEN_RECIPES,
    )
    text = models.TextField(
        "Описание рецепта",
    )
    cooking_time = models.PositiveIntegerField(
        "Время приготовления",
        default=1,
        validators=(MinValueValidator(1, "Минимум 1 минута"),),
    )
    pub_date = models.DateTimeField("Дата публикации рецепта", auto_now_add=True)

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"
        ordering = ("-pub_date",)
        constraints = (
            models.UniqueConstraint(
                fields=("name", "author"), name="unique_for_author"
            ),
        )

    def __str__(self):
        return f"Автор: {self.author.username} рецепт: {self.name}"


class IngredientAmount(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="recipe",
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name="ingredient",
    )
    amount = models.PositiveIntegerField(
        "Количество",
        default=1,
        validators=(MinValueValidator(1, "Минимум 1"),),
    )

    class Meta:
        ordering = ("id",)
        verbose_name = "Количество ингредиента"
        verbose_name_plural = "Количество ингредиентов"
        constraints = [
            models.UniqueConstraint(
                fields=("recipe", "ingredient"), name="unique ingredient"
            )
        ]

    def __str__(self):
        return (
            f"В рецепте {self.recipe.name} {self.amount}"
            f"{self.ingredient.measurement_unit} {self.ingredient.name}"
        )


class FavoriteRecipe(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="favorite",
        verbose_name="Пользователь",
    )
    favorite_recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="favorite_recipe",
        verbose_name="Избранный рецепт",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=("user", "favorite_recipe"), name="unique favourite"
            )
        ]
        verbose_name = "Избранное"
        verbose_name_plural = "Избранные"
        ordering = ("id",)

    def __str__(self):
        return f"Пользователь: {self.user.username} рецепт: {self.favorite_recipe.name}"


class Subscribe(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="follower",
        verbose_name="Подписчик",
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="following", verbose_name="Автор"
    )
    created = models.DateTimeField("Дата подписки", auto_now_add=True)

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
        ordering = ("-id",)
        constraints = [
            models.UniqueConstraint(
                fields=("user", "author"), name="unique_subscription"
            )
        ]

    def __str__(self):
        return f"Пользователь: {self.user.username} автор: {self.author.username}"


class ShoppingCart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="shopping_cart",
        verbose_name="Пользователь",
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="recipe_shopping_cart",
        verbose_name="Рецепт",
    )

    class Meta:
        ordering = ("id",)
        constraints = [
            models.UniqueConstraint(
                fields=("user", "recipe"), name="unique recipe in shopping cart"
            )
        ]
        verbose_name = "Список покупок"
        verbose_name_plural = "Список покупок"

    def __str__(self):
        return (
            f"Пользователь: {self.user.username},"
            f"рецепт в списке: {self.recipe.name}"
        )
