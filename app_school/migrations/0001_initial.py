# Generated by Django 4.2.7 on 2023-12-14 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chiefs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ceo_position', models.CharField(choices=[('3', 'Vice director for scientific affairs'), ('2', 'Vice director for academic affairs'), ('1', 'Director')], max_length=50, verbose_name='Position')),
                ('ceo_fullname', models.CharField(max_length=60, verbose_name='Full name')),
                ('ceo_phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone number')),
                ('ceo_email', models.EmailField(blank=True, max_length=50, null=True, verbose_name='Email')),
                ('ceo_prime_day', models.CharField(choices=[('4', 'Thursday'), ('6', 'Saturday'), ('2', 'Tuesday'), ('3', 'Wednesday'), ('5', 'Friday'), ('1', 'Monday')], max_length=10, verbose_name='Prime days')),
                ('ceo_prime_time', models.CharField(max_length=15, verbose_name='Prime time')),
                ('ceo_image', models.ImageField(upload_to='ceo', verbose_name='Image')),
                ('ceo_desc', models.CharField(max_length=300, verbose_name='Description')),
            ],
            options={
                'db_table': 'school_chiefs',
                'ordering': ['ceo_position'],
            },
        ),
    ]
