# Generated by Django 3.0.3 on 2020-03-23 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_category_sub_cat'),
    ]

    operations = [
        migrations.CreateModel(
            name='view_room_db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=100)),
                ('sub_category', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('fileup', models.CharField(max_length=50)),
                ('room_price', models.IntegerField()),
                ('room_facility', models.CharField(max_length=50)),
            ],
        ),
    ]