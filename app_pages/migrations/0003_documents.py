# Generated by Django 4.2.7 on 2023-12-05 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_pages', '0002_alter_aboutschool_school_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_title_uz', models.CharField(max_length=255, verbose_name='Hujjat nomi')),
                ('doc_title_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Document title')),
                ('doc_title_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название документа')),
                ('doc_type', models.CharField(choices=[(4, 'Buyruq'), (2, 'Qaror'), (5, 'Farmon'), (1, 'Qonun'), (3, 'Farmoyish')], max_length=15, verbose_name='Toifa/Type')),
                ('doc_org', models.CharField(choices=[(4, 'Xalq talimi vazirligi'), (1, 'Parlament'), (3, 'Vazirlar mahkamasi'), (5, 'Boshqarma'), (2, 'Prezident')], max_length=25, verbose_name='Tashkilot/Organisation')),
                ('doc_code', models.CharField(max_length=50, verbose_name='№')),
                ('doc_date', models.DateField(verbose_name='Hujjat qabul qilingan vaqt')),
                ('doc_link', models.URLField(blank=True, max_length=500, null=True, verbose_name='Hujjat matni havolasi')),
            ],
            options={
                'db_table': 'documents',
            },
        ),
    ]
