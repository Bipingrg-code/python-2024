# Generated by Django 5.0.1 on 2024-01-26 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('roll', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
    ]
