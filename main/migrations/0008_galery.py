# Generated by Django 5.1.1 on 2024-09-24 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_works'),
    ]

    operations = [
        migrations.CreateModel(
            name='Galery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=230)),
                ('nomi', models.CharField(max_length=120)),
                ('img', models.ImageField(upload_to='media/')),
            ],
        ),
    ]
