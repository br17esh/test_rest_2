# Generated by Django 2.1.5 on 2019-06-02 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dqrreport', '0018_auto_20190602_0504'),
    ]

    operations = [
        migrations.AddField(
            model_name='pixelprop',
            name='PP_QD1_CNT',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pixelprop',
            name='PP_QD1_DID',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pixelprop',
            name='PP_QD1_PID',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pixelprop',
            name='PP_QD1_SG',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pixelprop',
            name='PP_QD2_CNT',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pixelprop',
            name='PP_QD2_DID',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pixelprop',
            name='PP_QD2_PID',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pixelprop',
            name='PP_QD2_SG',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pixelprop',
            name='PP_QD3_CNT',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pixelprop',
            name='PP_QD3_DID',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pixelprop',
            name='PP_QD3_PID',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pixelprop',
            name='PP_QD3_SG',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
