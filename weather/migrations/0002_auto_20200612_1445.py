# Generated by Django 2.2 on 2020-06-12 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='fixedItems',
        ),
        migrations.DeleteModel(
            name='seasonalItems',
        ),
    ]
