# Generated by Django 4.2.1 on 2023-05-26 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appi', '0004_ventas_id_alter_ventas_numero_ventas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ventas',
            name='id',
        ),
        migrations.AlterField(
            model_name='ventas',
            name='numero_ventas',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
