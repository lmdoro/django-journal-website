# Generated by Django 3.0.2 on 2020-01-24 14:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0008_auto_20200124_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.get_current_timezone),
        ),
    ]
