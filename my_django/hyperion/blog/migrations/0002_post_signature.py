# Generated by Django 4.2 on 2023-04-20 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='signature',
            field=models.CharField(default='If at first you dont succeed, lower your standards.', max_length=140),
        ),
    ]
