# Generated by Django 3.2.9 on 2021-11-24 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_film_release_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='director',
            name='sex',
            field=models.CharField(blank=True, choices=[('m', 'Male'), ('f', 'Female'), ('o', 'Other')], default='o', help_text='(M/F/O)', max_length=1),
        ),
    ]