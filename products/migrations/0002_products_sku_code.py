# Generated by Django 3.0.5 on 2020-04-27 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='sku_code',
            field=models.CharField(default='abc', max_length=50, unique=True),
            preserve_default=False,
        ),
    ]
