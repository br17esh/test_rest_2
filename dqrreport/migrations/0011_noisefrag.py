# Generated by Django 2.1.5 on 2019-05-30 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dqrreport', '0010_datasat'),
    ]

    operations = [
        migrations.CreateModel(
            name='noisefrag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UID', models.CharField(max_length=200)),
                ('QA_S1B', models.CharField(max_length=200)),
                ('QA_B0C', models.CharField(max_length=200)),
                ('QA_B2KC', models.CharField(max_length=200)),
                ('QA_HRB', models.CharField(max_length=200)),
                ('QA_NTT', models.CharField(max_length=200)),
                ('QA_NDT', models.CharField(max_length=200)),
                ('QA_MLC', models.CharField(max_length=200)),
                ('QB_S1B', models.CharField(max_length=200)),
                ('QB_B0C', models.CharField(max_length=200)),
                ('QB_B2KC', models.CharField(max_length=200)),
                ('QB_HRB', models.CharField(max_length=200)),
                ('QB_NTT', models.CharField(max_length=200)),
                ('QB_NDT', models.CharField(max_length=200)),
                ('QB_MLC', models.CharField(max_length=200)),
                ('QC_S1B', models.CharField(max_length=200)),
                ('QC_B0C', models.CharField(max_length=200)),
                ('QC_B2KC', models.CharField(max_length=200)),
                ('QC_HRB', models.CharField(max_length=200)),
                ('QC_NTT', models.CharField(max_length=200)),
                ('QC_NDT', models.CharField(max_length=200)),
                ('QC_MLC', models.CharField(max_length=200)),
                ('QD_S1B', models.CharField(max_length=200)),
                ('QD_B0C', models.CharField(max_length=200)),
                ('QD_B2KC', models.CharField(max_length=200)),
                ('QD_HRB', models.CharField(max_length=200)),
                ('QD_NTT', models.CharField(max_length=200)),
                ('QD_NDT', models.CharField(max_length=200)),
                ('QD_MLC', models.CharField(max_length=200)),
            ],
        ),
    ]