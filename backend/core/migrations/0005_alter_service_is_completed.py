# Generated by Django 4.2.4 on 2023-09-08 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_service_is_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='is_completed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]