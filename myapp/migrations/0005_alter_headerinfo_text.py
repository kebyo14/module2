# Generated by Django 4.2.17 on 2025-01-18 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_headerinfo_alter_headernav_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headerinfo',
            name='text',
            field=models.CharField(max_length=500),
        ),
    ]
