# Generated by Django 3.2.5 on 2021-12-27 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traveller', '0002_destination_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='img',
            field=models.ImageField(default=0, upload_to='pics'),
            preserve_default=False,
        ),
    ]
