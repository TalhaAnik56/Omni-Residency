# Generated by Django 5.0.6 on 2024-05-27 18:33

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
        ('refuel', '0004_gym_area'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='gym',
            name='gender_allowance',
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
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='community.guest')),
            ],
        ),
    ]
