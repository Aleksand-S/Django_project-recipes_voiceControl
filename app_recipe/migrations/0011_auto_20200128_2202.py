# Generated by Django 2.2.8 on 2020-01-28 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_recipe', '0010_step'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='step',
            name='step_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
