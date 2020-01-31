# Generated by Django 3.0.2 on 2020-01-30 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('knihovna', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='isReturned',
        ),
        migrations.AlterField(
            model_name='book',
            name='bookDetail',
            field=models.TextField(max_length=500, verbose_name='Book description'),
        ),
        migrations.AlterField(
            model_name='book',
            name='bookName',
            field=models.CharField(max_length=100, verbose_name='Book name'),
        ),
        migrations.AlterField(
            model_name='book',
            name='bookWriter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='knihovna.Author', verbose_name="Author's name"),
        ),
        migrations.AlterField(
            model_name='book',
            name='bookYear',
            field=models.DateField(blank=True, null=True, verbose_name='Book release year'),
        ),
        migrations.AlterField(
            model_name='book',
            name='borrowedBy',
            field=models.CharField(blank=True, max_length=100, verbose_name='Borrowed by'),
        ),
        migrations.AlterField(
            model_name='book',
            name='borrowedDate',
            field=models.DateField(blank=True, null=True, verbose_name='Borrowed date'),
        ),
        migrations.AlterField(
            model_name='book',
            name='isBorrowed',
            field=models.BooleanField(default=False, verbose_name='Currently borrowed'),
        ),
        migrations.AlterField(
            model_name='book',
            name='returnedDate',
            field=models.DateField(blank=True, null=True, verbose_name='Return date'),
        ),
    ]