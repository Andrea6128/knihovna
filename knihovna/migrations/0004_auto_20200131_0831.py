# Generated by Django 3.0.2 on 2020-01-31 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knihovna', '0003_auto_20200130_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='authorDetail',
            field=models.TextField(default='something', max_length=1000, verbose_name='Author description'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='authorName',
            field=models.CharField(max_length=100, verbose_name="Author's name"),
        ),
    ]