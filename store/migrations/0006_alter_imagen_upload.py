# Generated by Django 3.2.2 on 2021-05-29 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20210513_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagen',
            name='upload',
            field=models.FileField(upload_to='media/'),
        ),
    ]
