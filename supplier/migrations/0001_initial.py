# Generated by Django 3.0.5 on 2020-04-25 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('supplier_code', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True)),
                ('primary_phone', models.CharField(max_length=15)),
                ('secondary_phone', models.CharField(blank=True, max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('additional_email', models.EmailField(blank=True, max_length=254)),
                ('address', models.TextField()),
                ('additional_address', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
