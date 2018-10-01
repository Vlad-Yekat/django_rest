# Generated by Django 2.0.3 on 2018-09-27 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('insidepages', '0003_auto_20180927_2233'),
    ]

    operations = [
        migrations.CreateModel(
            name='AudioVer2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bit_rate', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PostVer2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.SlugField()),
                ('counter', models.IntegerField(default=0)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='TextVer2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VideoVer2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_video', models.CharField(max_length=250)),
                ('ref_subs', models.CharField(max_length=250)),
            ],
        ),
    ]