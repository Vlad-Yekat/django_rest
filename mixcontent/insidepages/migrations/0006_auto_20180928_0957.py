# Generated by Django 2.1.1 on 2018-09-28 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insidepages', '0005_auto_20180928_0008'),
    ]

    operations = [
        migrations.AddField(
            model_name='textver2',
            name='short',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AlterField(
            model_name='textver2',
            name='text',
            field=models.TextField(default='-'),
        ),
    ]
