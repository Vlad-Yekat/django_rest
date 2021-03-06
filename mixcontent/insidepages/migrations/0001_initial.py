# Generated by Django 2.1.1 on 2018-09-19 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bitrate', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MixPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('counter', models.IntegerField(default=0)),
                ('type_content', models.CharField(max_length=10)),
                ('ref_content', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Texts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TextDetail', models.CharField(max_length=250, null=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insidepages.MixPost')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_video', models.CharField(max_length=250)),
                ('ref_subs', models.CharField(max_length=250)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insidepages.MixPost')),
            ],
        ),
        migrations.AddField(
            model_name='audio',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insidepages.MixPost'),
        ),
    ]
