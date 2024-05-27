# Generated by Django 5.0.6 on 2024-05-27 17:42

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refuel', '0002_reservation'),
        ('segment', '0003_rename_room_type_booking_room_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Gym',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('A', 'Active'), ('O', 'Out of order')], default='A', max_length=1)),
                ('overview', models.TextField()),
                ('gender_allowance', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
                ('fees', models.DecimalField(decimal_places=2, max_digits=9)),
                ('opening', models.TimeField()),
                ('closing', models.TimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='segment.branch')),
            ],
        ),
    ]
