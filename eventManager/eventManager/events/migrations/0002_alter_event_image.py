# Generated by Django 5.1.3 on 2024-11-26 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
