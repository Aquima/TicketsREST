# Generated by Django 2.0.5 on 2018-05-28 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_auto_20180528_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='enum_type',
            field=models.IntegerField(choices=[('MUS', 'Music'), ('MOV', 'Movie'), ('CON', 'Conference')], max_length=3),
        ),
    ]
