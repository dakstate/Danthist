# Generated by Django 2.1.1 on 2019-01-23 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0008_merge_20190123_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='StajR',
            field=models.CharField(max_length=15, verbose_name='Стаж'),
        ),
    ]