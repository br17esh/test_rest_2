# Generated by Django 2.1.5 on 2019-02-08 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dqrreport', '0003_dph_uid'),
    ]

    operations = [
        migrations.CreateModel(
            name='obsinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_obs', models.CharField(max_length=50)),
                ('time_obs', models.CharField(max_length=50)),
                ('date_end', models.CharField(max_length=50)),
                ('time_end', models.CharField(max_length=50)),
                ('obs_id', models.CharField(max_length=50)),
                ('exposure', models.CharField(max_length=50)),
                ('sourceid', models.CharField(max_length=50)),
                ('observer', models.CharField(max_length=50)),
                ('ra_pnt', models.CharField(max_length=50)),
                ('dec_pnt', models.CharField(max_length=50)),
            ],
        ),
    ]
