# Generated by Django 4.0 on 2022-01-20 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0004_rename_почта_subscriber_email_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscriber',
            options={'verbose_name': 'Подписчик', 'verbose_name_plural': 'Подписчики'},
        ),
    ]
