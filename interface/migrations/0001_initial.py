# Generated by Django 5.0.2 on 2024-02-18 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('paddress', models.CharField(max_length=255)),
                ('taddress', models.CharField(max_length=255)),
                ('pnum', models.CharField(max_length=255)),
                ('dob', models.CharField(max_length=255)),
                ('timestamp', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]
