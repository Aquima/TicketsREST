# Generated by Django 2.0.5 on 2018-05-28 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_auto_20180528_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='code',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='name',
            field=models.CharField(default='', max_length=150),
        ),
    ]
