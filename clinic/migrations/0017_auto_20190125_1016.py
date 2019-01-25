# Generated by Django 2.1.1 on 2019-01-25 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0016_merge_20190124_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Img',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Ссылка картинки'),
        ),
        migrations.AddField(
            model_name='user',
            name='Type',
            field=models.CharField(choices=[('V', 'Врач'), ('S', 'Секретарь')], default=1, max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='StajR',
            field=models.CharField(max_length=15, verbose_name='Стаж'),
        ),
    ]
