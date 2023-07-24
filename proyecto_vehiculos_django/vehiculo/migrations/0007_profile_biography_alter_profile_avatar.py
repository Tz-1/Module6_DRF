# Generated by Django 4.0.5 on 2023-07-24 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0006_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='biography',
            field=models.TextField(default='blank', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='profile_avatars/avatar.jpg', upload_to='profile_avatars'),
        ),
    ]
