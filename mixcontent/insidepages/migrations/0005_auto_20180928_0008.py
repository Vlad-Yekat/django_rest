# Generated by Django 2.0.3 on 2018-09-27 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insidepages', '0004_audiover2_postver2_textver2_videover2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postver2',
            name='title',
            field=models.CharField(max_length=120),
        ),
    ]