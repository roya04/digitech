# Generated by Django 5.0.3 on 2024-03-11 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0005_alter_campaign_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='discount_percent',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
