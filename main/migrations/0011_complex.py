# Generated by Django 5.1.1 on 2024-09-25 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_process'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sana', models.CharField(max_length=120)),
                ('title', models.CharField(max_length=230)),
                ('nomi', models.CharField(max_length=120)),
                ('text', models.TextField()),
                ('img', models.ImageField(upload_to='media/')),
            ],
        ),
    ]
