# Generated by Django 3.1.7 on 2021-03-12 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_hobby_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='category',
        ),
    ]
