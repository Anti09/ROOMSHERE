# Generated by Django 3.0.3 on 2020-03-29 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_view_room_db'),
    ]

    operations = [
        migrations.CreateModel(
            name='image_upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_upload', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='view_room_db',
            name='fileup',
        ),
    ]
