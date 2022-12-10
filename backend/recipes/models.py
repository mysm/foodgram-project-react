from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

MAX_LEN_RECIPES = 255

User = get_user_model()


class MeasurementUnits(models.Model):
    """ Единицы измерения"""

    name = models.CharField(
        verbose_name='Единица измерения',
        max_length=MAX_LEN_RECIPES,
        unique=True,
    )

    class Meta:
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'
        ordering = ('name',)


class Tag(models.Model):
    name = models.CharField(
        verbose_name='Название тега',
        max_length=MAX_LEN_RECIPES,
        unique=True,
    )
    color = models.CharField(
        verbose_name='Цветовой HEX-код',
        max_length=7,
        default='#00ff7f',
        null=True,
        blank=True,
        unique=True,
    )
    slug = models.SlugField(
        'Slug тега',
        max_length=MAX_LEN_RECIPES,
        unique=True,
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ('name',)

    def __str__(self):
        return self.name
