# Generated by Django 5.1.3 on 2024-12-09 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
    ]