# Generated by Django 3.1 on 2020-08-30 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colony', '0005_auto_20200825_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='apiary',
            name='primary_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]