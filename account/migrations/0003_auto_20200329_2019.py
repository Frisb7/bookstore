# Generated by Django 3.0.4 on 2020-03-29 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200329_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='grno',
            field=models.IntegerField(default=0),
        ),
    ]
