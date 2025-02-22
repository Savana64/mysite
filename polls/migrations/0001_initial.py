# Generated by Django 5.1 on 2024-09-08 11:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Otázka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otázka_text', models.CharField(max_length=200)),
                ('zveřejněná_data', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Čojz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('čojz_text', models.CharField(max_length=200)),
                ('volby', models.IntegerField(default=0)),
                ('otázka', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.otázka')),
            ],
        ),
    ]
