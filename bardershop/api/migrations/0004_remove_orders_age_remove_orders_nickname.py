# Generated by Django 4.2.6 on 2024-02-10 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_services_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='age',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='nickname',
        ),
    ]
