# Generated by Django 3.2.19 on 2023-06-07 20:35

from django.db import migrations, models
import django.db.models.deletion
import traffic.app.utils


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='camera',
            name='Кол-во адров в секунду',
        ),
        migrations.RemoveField(
            model_name='camera',
            name='Локация, на которой установлена камера',
        ),
        migrations.RemoveField(
            model_name='camera',
            name='Фокусное расстояние',
        ),
        migrations.RemoveField(
            model_name='location',
            name='Администратор',
        ),
        migrations.RemoveField(
            model_name='location',
            name='Адрес локации для подсчета трафика',
        ),
        migrations.RemoveField(
            model_name='location',
            name='Клиент',
        ),
        migrations.RemoveField(
            model_name='report',
            name='JSON данные',
        ),
        migrations.RemoveField(
            model_name='report',
            name='Локация, на которой ведэтся подсчет',
        ),
        migrations.RemoveField(
            model_name='userfiles',
            name='Файл',
        ),
        migrations.AddField(
            model_name='camera',
            name='focus',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=3, null=True, verbose_name='Фокусное расстояние'),
        ),
        migrations.AddField(
            model_name='camera',
            name='fps',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=15, null=True, verbose_name='Кол-во адров в секунду'),
        ),
        migrations.AddField(
            model_name='camera',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='location_camera', to='app.location', verbose_name='Локация, на которой установлена камера'),
        ),
        migrations.AddField(
            model_name='location',
            name='address',
            field=models.TextField(blank=True, null=True, verbose_name='Адрес локации для подсчета трафика'),
        ),
        migrations.AddField(
            model_name='location',
            name='admin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='location_admin', to='app.user', verbose_name='Администратор'),
        ),
        migrations.AddField(
            model_name='location',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='location', to='app.user', verbose_name='Клиент'),
        ),
        migrations.AddField(
            model_name='report',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='location_report', to='app.location', verbose_name='Локация, на которой ведэтся подсчет'),
        ),
        migrations.AddField(
            model_name='report',
            name='model_report',
            field=models.TextField(blank=True, null=True, verbose_name='JSON данные'),
        ),
        migrations.AddField(
            model_name='userfiles',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=traffic.app.utils.get_file_path, verbose_name='Файл'),
        ),
    ]
