# Generated by Django 3.1.7 on 2021-04-01 18:18

from django.db import migrations, models
import users.utils


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='display_photo',
            field=models.ImageField(default='text', upload_to=users.utils.upload_image_path, verbose_name='Display Photo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, verbose_name='Gender'),
        ),
    ]
