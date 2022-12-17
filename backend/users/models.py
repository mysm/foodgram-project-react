from django.contrib.auth.models import AbstractUser
from django.db import models

MAX_LEN_USER = 255


class User(AbstractUser):
    """Пользователи"""

    username = models.CharField(
        verbose_name="Логин",
        max_length=MAX_LEN_USER,
        unique=True,
    )
    email = models.EmailField(
        verbose_name="Email",
        max_length=MAX_LEN_USER,
        unique=True,
    )
    first_name = models.CharField(
        verbose_name="Имя",
        max_length=MAX_LEN_USER,
    )
    last_name = models.CharField(
        verbose_name="Фамилия",
        max_length=MAX_LEN_USER,
    )
    subscribe = models.ManyToManyField(
        verbose_name='Подписка',
        related_name='subscribers',
        to='self',
        symmetrical=False,
    )

    class Meta:
        ordering = ("username",)
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.username}, {self.email}"
