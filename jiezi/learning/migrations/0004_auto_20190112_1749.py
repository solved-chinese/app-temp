# Generated by Django 2.1.2 on 2019-01-12 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0003_auto_20190110_2144'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='character',
            unique_together={('chinese', 'english')},
        ),
    ]