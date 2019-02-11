# Generated by Django 2.1.5 on 2019-02-04 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dqrstats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename_OF', models.CharField(max_length=50)),
                ('filename_FF', models.CharField(max_length=50)),
                ('size_bytes_OF', models.CharField(max_length=50)),
                ('size_bytes_FF', models.CharField(max_length=50)),
                ('size_OF', models.CharField(max_length=50)),
                ('size_FF', models.CharField(max_length=50)),
                ('events_quadA_OF', models.CharField(max_length=50)),
                ('events_quadA_FF', models.CharField(max_length=50)),
                ('events_quadB_OF', models.CharField(max_length=50)),
                ('events_quadB_FF', models.CharField(max_length=50)),
                ('events_quadC_OF', models.CharField(max_length=50)),
                ('events_quadC_FF', models.CharField(max_length=50)),
                ('events_quadD_OF', models.CharField(max_length=50)),
                ('events_quadD_FF', models.CharField(max_length=50)),
            ],
        ),
    ]
