# Generated by Django 2.0.5 on 2018-05-28 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0007_auto_20180528_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='name',
        ),
    ]
