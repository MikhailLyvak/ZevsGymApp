# Generated by Django 5.0.2 on 2024-04-10 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jum_app', '0004_repeat_hurd_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dayexercise',
            options={'ordering': ['-date', 'exercise'], 'verbose_name': 'Впава на день', 'verbose_name_plural': 'Вправи на день'},
        ),
        migrations.AlterModelOptions(
            name='repeat',
            options={'ordering': ['id', 'day_exercise', 'repeats'], 'verbose_name': 'Підхід', 'verbose_name_plural': 'Підходи'},
        ),
        migrations.AddField(
            model_name='dayexercise',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='repeat',
            name='hurd_type',
            field=models.CharField(choices=[('Отказ', 'Отказ'), ('Дуже складно', 'Дуже складно'), ('Ідеально', 'Ідеально'), ('Залегко', 'Залегко')], max_length=255),
        ),
    ]
