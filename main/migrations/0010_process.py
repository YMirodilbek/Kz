# Generated by Django 5.1.1 on 2024-09-25 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_stay'),
    ]

    operations = [
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sana', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=120)),
                ('nomi', models.CharField(max_length=1230)),
                ('text', models.TextField()),
                ('img', models.ImageField(upload_to='media/')),
            ],
        ),
    ]
