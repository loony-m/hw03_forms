# Generated by Django 2.2.19 on 2022-10-21 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20221020_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='slub',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='group',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]