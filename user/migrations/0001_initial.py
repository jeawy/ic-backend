# Generated by Django 5.2b1 on 2025-03-11 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
            ],
        ),
    ]
