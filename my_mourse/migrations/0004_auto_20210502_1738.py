# Generated by Django 2.2.14 on 2021-05-02 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_mourse', '0003_auto_20210502_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mourse',
            name='slug',
            field=models.SlugField(default='change-me', unique=True),
        ),
    ]
