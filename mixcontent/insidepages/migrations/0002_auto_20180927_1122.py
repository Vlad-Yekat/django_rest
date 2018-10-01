# Generated by Django 2.1.1 on 2018-09-27 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insidepages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mixpost',
            options={'verbose_name': 'Page with posts'},
        ),
        migrations.RenameField(
            model_name='audio',
            old_name='bitrate',
            new_name='bit_rate',
        ),
        migrations.AddField(
            model_name='texts',
            name='FullText',
            field=models.TextField(blank=True, null=True),
        ),
    ]