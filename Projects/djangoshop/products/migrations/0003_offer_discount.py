# Generated by Django 5.0.1 on 2024-01-24 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='discount',
            field=models.FloatField(default=0.0),
        ),
    ]
