# Generated by Django 4.2.1 on 2023-06-16 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_namegame_keygame'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.namegame', verbose_name='Название'),
        ),
    ]