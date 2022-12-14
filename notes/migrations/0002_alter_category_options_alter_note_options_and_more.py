# Generated by Django 4.1 on 2022-08-16 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='note',
            options={'verbose_name': 'Note', 'verbose_name_plural': 'Notes'},
        ),
        migrations.RemoveField(
            model_name='note',
            name='category',
        ),
        migrations.AddField(
            model_name='note',
            name='category',
            field=models.ManyToManyField(to='notes.category'),
        ),
    ]
