# Generated by Django 5.0.2 on 2024-02-25 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jum_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='repeat',
            options={'ordering': ['day_exercise', 'repeats'], 'verbose_name': 'Впава на день', 'verbose_name_plural': 'Вправи на день'},
        ),
        migrations.RemoveIndex(
            model_name='repeat',
            name='jum_app_rep_id_5a1910_idx',
        ),
        migrations.RemoveIndex(
            model_name='repeat',
            name='jum_app_rep_approac_32584f_idx',
        ),
        migrations.RemoveField(
            model_name='repeat',
            name='approach',
        ),
        migrations.AddIndex(
            model_name='repeat',
            index=models.Index(fields=['id', 'day_exercise', 'repeats'], name='jum_app_rep_id_c428b7_idx'),
        ),
    ]