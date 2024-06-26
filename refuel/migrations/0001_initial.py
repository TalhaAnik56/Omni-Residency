# Generated by Django 5.0.6 on 2024-05-27 18:45

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('community', '0001_initial'),
        ('segment', '0003_rename_room_type_booking_room_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gym',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('A', 'Active'), ('O', 'Out of order')], default='A', max_length=1)),
                ('overview', models.TextField()),
                ('area', models.PositiveSmallIntegerField(default=0)),
                ('fees', models.DecimalField(decimal_places=2, max_digits=9)),
                ('opening', models.TimeField()),
                ('closing', models.TimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='segment.branch')),
            ],
        ),
        migrations.CreateModel(
            name='GymGender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='gender_allowance', to='refuel.gender')),
                ('gym', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='refuel.gym')),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('mobile', models.CharField(max_length=14, validators=[django.core.validators.RegexValidator(message='Enter a valid Bangladeshi mobile number.', regex='^\\+880?\\d{10}$|^0\\d{10}$')])),
                ('fees', models.DecimalField(decimal_places=2, max_digits=9)),
                ('status', models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('D', 'Declined')], default='P', max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='community.guest')),
                ('gym', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='refuel.gym')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('A', 'Active'), ('O', 'Out of order')], default='A', max_length=1)),
                ('overview', models.TextField()),
                ('breakfast_opening', models.TimeField()),
                ('breakfast_closing', models.TimeField()),
                ('lunch_opening', models.TimeField()),
                ('lunch_closing', models.TimeField()),
                ('dinner_opening', models.TimeField()),
                ('dinner_closing', models.TimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='segment.branch')),
                ('cuisine', models.ManyToManyField(to='refuel.cuisine')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PEN', 'Pending'), ('CON', 'Confirmed'), ('COM', 'Completed'), ('CAN', 'Cancelled')], default='PEN', max_length=3)),
                ('guest_name', models.CharField(max_length=50)),
                ('guest_email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=14, validators=[django.core.validators.RegexValidator(message='Enter a valid Bangladeshi mobile number.', regex='^\\+880?\\d{10}$|^0\\d{10}$')])),
                ('number_of_people', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('reservation_date', models.DateField()),
                ('reservation_time', models.TimeField()),
                ('additional_info', models.TextField(blank=True, null=True)),
                ('total_bill', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='refuel.restaurant')),
            ],
        ),
    ]
