# Generated by Django 4.2.6 on 2024-02-10 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='services',
            options={'ordering': ['title'], 'verbose_name': 'Услуга', 'verbose_name_plural': 'Услуги'},
        ),
    ]
