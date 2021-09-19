# Generated by Django 3.2 on 2021-05-20 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0002_delete_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(max_length=300, upload_to='car')),
                ('title', models.CharField(max_length=200)),
                ('stock', models.IntegerField(default=2)),
            ],
        ),
    ]
