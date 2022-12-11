# Generated by Django 4.1.3 on 2022-12-11 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0004_amountingredient_recipe_amountingredient_recipe_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tag",
            name="color",
            field=models.CharField(
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
    ]
