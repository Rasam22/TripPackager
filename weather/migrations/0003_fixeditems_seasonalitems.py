# Generated by Django 2.2 on 2020-06-12 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_auto_20200612_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='fixedItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='seasonalItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=50)),
                ('season', models.CharField(max_length=50)),
            ],
        ),
    ]
