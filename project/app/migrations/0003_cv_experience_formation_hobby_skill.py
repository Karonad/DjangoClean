# Generated by Django 3.1.7 on 2021-03-12 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastname', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('age', models.IntegerField()),
                ('permis', models.BooleanField()),
                ('city', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('level', models.IntegerField()),
                ('cv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cv')),
            ],
        ),
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=500)),
                ('cv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cv')),
            ],
        ),
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=500)),
                ('start_at', models.DateTimeField()),
                ('end_at', models.DateTimeField()),
                ('cv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cv')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=500)),
                ('start_at', models.DateTimeField()),
                ('end_at', models.DateTimeField()),
                ('cv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cv')),
            ],
        ),
    ]