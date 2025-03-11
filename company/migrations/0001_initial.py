# Generated by Django 5.2b1 on 2025-03-11 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('new', 'New'), ('approved', 'Approved'), ('pending', 'Pending'), ('rejected', 'Rejected'), ('disabled', 'Disabled')], default='new', max_length=10)),
            ],
        ),
    ]
