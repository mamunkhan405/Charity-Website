# Generated by Django 3.1.4 on 2021-02-18 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charityApp', '0002_members_mem_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='mem_email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
