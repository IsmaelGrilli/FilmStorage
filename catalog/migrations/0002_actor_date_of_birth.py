# Generated by Django 3.2.9 on 2021-11-24 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
