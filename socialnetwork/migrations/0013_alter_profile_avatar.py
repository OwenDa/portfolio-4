# Generated by Django 3.2.13 on 2022-08-04 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialnetwork', '0012_rename_iduser_profile_id_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='default-user_vltu5x', upload_to='avatars/', verbose_name='image'),
        ),
    ]
