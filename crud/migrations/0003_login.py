# Generated by Django 3.0 on 2020-01-07 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_auto_20200106_1422'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=8)),
            ],
        ),
    ]
