# Generated by Django 4.2.15 on 2024-11-15 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinalUrls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scan_id', models.IntegerField()),
                ('url', models.URLField()),
                ('status', models.IntegerField(null=True)),
            ],
        ),
    ]
