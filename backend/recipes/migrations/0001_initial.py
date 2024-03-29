# Generated by Django 4.1.3 on 2022-12-25 20:04

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="FavoriteRecipe",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "verbose_name": "Избранное",
                "verbose_name_plural": "Избранные",
                "ordering": ("id",),
            },
        ),
        migrations.CreateModel(
            name="Ingredient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=255, verbose_name="Название ингредиента"
                    ),
                ),
                (
                    "measurement_unit",
                    models.CharField(
                        max_length=255, verbose_name="Единицы измерения"
                    ),
                ),
            ],
            options={
                "verbose_name": "Ингредиент",
                "verbose_name_plural": "Ингредиенты",
                "ordering": ("id",),
            },
        ),
        migrations.CreateModel(
            name="IngredientAmount",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "amount",
                    models.PositiveIntegerField(
                        default=1,
                        validators=[
                            django.core.validators.MinValueValidator(
                                1, "Минимум 1"
                            )
                        ],
                        verbose_name="Количество",
                    ),
                ),
                (
                    "ingredient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ingredient",
                        to="recipes.ingredient",
                    ),
                ),
            ],
            options={
                "verbose_name": "Количество ингредиента",
                "verbose_name_plural": "Количество ингредиентов",
                "ordering": ("id",),
            },
        ),
        migrations.CreateModel(
            name="Recipe",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to="recipes/images",
                        verbose_name="Изображение рецепта",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=255, verbose_name="Название рецепта"
                    ),
                ),
                ("text", models.TextField(verbose_name="Описание рецепта")),
                (
                    "cooking_time",
                    models.PositiveIntegerField(
                        default=1,
                        validators=[
                            django.core.validators.MinValueValidator(
                                1, "Минимум 1 минута"
                            )
                        ],
                        verbose_name="Время приготовления",
                    ),
                ),
                (
                    "pub_date",
                    models.DateTimeField(
                        auto_now_add=True,
                        verbose_name="Дата публикации рецепта",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="recipe",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор рецепта",
                    ),
                ),
                (
                    "ingredients",
                    models.ManyToManyField(
                        through="recipes.IngredientAmount",
                        to="recipes.ingredient",
                        verbose_name="Ингредиенты",
                    ),
                ),
            ],
            options={
                "verbose_name": "Рецепт",
                "verbose_name_plural": "Рецепты",
                "ordering": ("-pub_date",),
            },
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=255,
                        unique=True,
                        verbose_name="Название тега",
                    ),
                ),
                (
                    "color",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("#0000FF", "Синий"),
                            ("#FFA500", "Оранжевый"),
                            ("#008000", "Зеленый"),
                            ("#800080", "Фиолетовый"),
                            ("#FFFF00", "Желтый"),
                            ("#FF0000", "Красный"),
                        ],
                        default="#008000",
                        max_length=7,
                        null=True,
                        unique=True,
                        verbose_name="Цветовой HEX-код",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        max_length=255, unique=True, verbose_name="Slug тега"
                    ),
                ),
            ],
            options={
                "verbose_name": "Тег",
                "verbose_name_plural": "Теги",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Subscribe",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата подписки"
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="following",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="follower",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Подписчик",
                    ),
                ),
            ],
            options={
                "verbose_name": "Подписка",
                "verbose_name_plural": "Подписки",
                "ordering": ("-id",),
            },
        ),
        migrations.CreateModel(
            name="ShoppingCart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "recipe",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="recipe_shopping_cart",
                        to="recipes.recipe",
                        verbose_name="Рецепт",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="shopping_cart",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Список покупок",
                "verbose_name_plural": "Список покупок",
                "ordering": ("id",),
            },
        ),
        migrations.AddField(
            model_name="recipe",
            name="tags",
            field=models.ManyToManyField(
                related_name="recipes", to="recipes.tag", verbose_name="Тег"
            ),
        ),
        migrations.AddField(
            model_name="ingredientamount",
            name="recipe",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="recipe",
                to="recipes.recipe",
            ),
        ),
        migrations.AddConstraint(
            model_name="ingredient",
            constraint=models.UniqueConstraint(
                fields=("name", "measurement_unit"),
                name="unique_name_measurement",
            ),
        ),
        migrations.AddField(
            model_name="favoriterecipe",
            name="favorite_recipe",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="favorite_recipe",
                to="recipes.recipe",
                verbose_name="Избранный рецепт",
            ),
        ),
        migrations.AddField(
            model_name="favoriterecipe",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="favorite",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь",
            ),
        ),
        migrations.AddConstraint(
            model_name="subscribe",
            constraint=models.UniqueConstraint(
                fields=("user", "author"), name="unique_subscription"
            ),
        ),
        migrations.AddConstraint(
            model_name="shoppingcart",
            constraint=models.UniqueConstraint(
                fields=("user", "recipe"),
                name="unique recipe in shopping cart",
            ),
        ),
        migrations.AddConstraint(
            model_name="ingredientamount",
            constraint=models.UniqueConstraint(
                fields=("recipe", "ingredient"), name="unique ingredient"
            ),
        ),
        migrations.AddConstraint(
            model_name="favoriterecipe",
            constraint=models.UniqueConstraint(
                fields=("user", "favorite_recipe"), name="unique favourite"
            ),
        ),
    ]
