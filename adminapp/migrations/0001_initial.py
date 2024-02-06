# Generated by Django 4.0.6 on 2022-07-07 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MessageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('subject', models.TextField(max_length=100)),
                ('product_description', models.TextField(max_length=225)),
            ],
            options={
                'db_table': 'message',
            },
        ),
    ]