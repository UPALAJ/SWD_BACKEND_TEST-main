# Generated by Django 5.0.2 on 2024-03-15 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todolistmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(blank=True, null=True, verbose_name='Created Date')),
                ('updated_date', models.DateField(blank=True, null=True, verbose_name='Updated Date')),
                ('element', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Element')),
            ],
        ),
    ]
