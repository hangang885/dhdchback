# Generated by Django 5.0.3 on 2024-03-20 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dhdch', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.TextField(max_length=10, unique=True),
        ),
    ]
