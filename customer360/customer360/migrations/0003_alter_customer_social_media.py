# Generated by Django 5.1.4 on 2024-12-06 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer360', '0002_customer_social_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='social_media',
            field=models.CharField(default='Something', max_length=100),
        ),
    ]
