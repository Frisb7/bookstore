# Generated by Django 3.0.4 on 2020-03-31 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_log_action'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='action',
            field=models.CharField(choices=[('Added to cart', 'Added to cart'), ('Removed from cart', 'Removed from cart'), ('Bought', 'Bought')], max_length=100),
        ),
    ]
