# Generated by Django 4.2.9 on 2024-02-18 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_cp', '0003_alter_user_car_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='car_name',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='app_cp.car'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='tel',
            field=models.CharField(max_length=15, verbose_name='Телефон'),
        ),
    ]