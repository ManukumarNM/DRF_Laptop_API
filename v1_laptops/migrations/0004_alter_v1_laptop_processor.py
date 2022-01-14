# Generated by Django 3.2.11 on 2022-01-12 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1_laptops', '0003_auto_20220112_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='v1_laptop',
            name='processor',
            field=models.CharField(choices=[('AMD Dual Core Ryzen', 'AMD Dual Core Ryzen'), ('Intel Dual Core', 'Intel Dual Core'), ('Intel 8 Core', 'Intel 8 Core'), ('Core i3', 'Core i3'), ('Core i5', 'Core i5'), ('Core i7', 'Core i7'), ('Core i10', 'Core i10')], default='Corei3', max_length=50),
        ),
    ]
