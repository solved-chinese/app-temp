# Generated by Django 2.1.7 on 2019-09-22 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0003_auto_20190707_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='structure',
            field=models.IntegerField(null=True),
        ),
    ]
