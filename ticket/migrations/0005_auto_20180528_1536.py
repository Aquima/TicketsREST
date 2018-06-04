# Generated by Django 2.0.5 on 2018-05-28 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0004_auto_20180528_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='enum_type',
            field=models.CharField(choices=[('MUS', 'Music'), ('MOV', 'Movie'), ('CON', 'Conference')], max_length=3),
        ),
    ]