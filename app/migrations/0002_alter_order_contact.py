# Generated by Django 4.2.3 on 2023-12-07 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='contact',
            field=models.IntegerField(),
        ),
    ]
