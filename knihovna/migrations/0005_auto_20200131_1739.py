# Generated by Django 3.0.2 on 2020-01-31 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knihovna', '0004_auto_20200131_0831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='isBorrowed',
        ),
        migrations.AlterField(
            model_name='book',
            name='borrowedDate',
            field=models.DateField(blank=True, null=True, verbose_name='Borrowed on'),
        ),
        migrations.AlterField(
            model_name='book',
            name='returnDate',
            field=models.DateField(blank=True, null=True, verbose_name='Will be returned on'),
        ),
    ]
