# Generated by Django 4.1.4 on 2022-12-13 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]
