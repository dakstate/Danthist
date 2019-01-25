# Generated by Django 2.1.2 on 2019-01-24 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0010_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=40)),
                ('quary', models.CharField(max_length=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='Type',
        ),
        migrations.AlterField(
            model_name='user',
            name='StajR',
            field=models.CharField(max_length=15, verbose_name='должность'),
        ),
    ]
