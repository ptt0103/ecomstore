# Generated by Django 4.1.7 on 2023-03-28 09:38

import comment_model.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='comment_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=50)),
                ('userId', models.CharField(max_length=50)),
                ('userName', models.CharField(max_length=12)),
                ('dateComment', comment_model.models.CustomDateTimeField(auto_now_add=True)),
            ],
        ),
    ]