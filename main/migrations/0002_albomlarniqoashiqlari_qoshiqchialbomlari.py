# Generated by Django 5.0.6 on 2024-06-25 06:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbomlarniQoashiqlari',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('albom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.albom')),
                ('qoshiq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.qoshiq')),
            ],
        ),
        migrations.CreateModel(
            name='QoshiqchiAlbomlari',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('albom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.albom')),
                ('qoshiqchi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.qoshiqchi')),
            ],
        ),
    ]
