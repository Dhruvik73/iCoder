# Generated by Django 4.0.2 on 2022-02-24 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blogpost_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='slug',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]