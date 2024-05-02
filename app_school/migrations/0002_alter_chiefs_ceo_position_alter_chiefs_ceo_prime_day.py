# Generated by Django 4.2.7 on 2023-12-14 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_school', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chiefs',
            name='ceo_position',
            field=models.CharField(choices=[('1', 'Director'), ('3', 'Vice director for scientific affairs'), ('2', 'Vice director for academic affairs')], max_length=50, verbose_name='Position'),
        ),
        migrations.AlterField(
            model_name='chiefs',
            name='ceo_prime_day',
            field=models.CharField(choices=[('6', 'Saturday'), ('4', 'Thursday'), ('2', 'Tuesday'), ('5', 'Friday'), ('3', 'Wednesday'), ('1', 'Monday')], max_length=10, verbose_name='Prime days'),
        ),
    ]
