# Generated by Django 2.0.5 on 2018-05-28 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('enum_type', models.IntegerField(max_length=2)),
                ('code', models.CharField(max_length=150)),
                ('title', models.TextField(blank=True, default='')),
                ('startTime', models.DateTimeField(auto_now=True)),
                ('endTime', models.DateTimeField(auto_now=True)),
                ('address', models.TextField(blank=True, default='')),
                ('date', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modify_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]