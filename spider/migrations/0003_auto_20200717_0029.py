# Generated by Django 3.0.8 on 2020-07-17 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spider', '0002_auto_20200717_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='userId',
            field=models.IntegerField(),
        ),
    ]