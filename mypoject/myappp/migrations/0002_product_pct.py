# Generated by Django 4.2.1 on 2024-09-30 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myappp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pct',
            field=models.ImageField(blank=True, upload_to='myappp/static/img'),
        ),
    ]
