# Generated by Django 5.0.3 on 2024-03-12 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0006_alter_campaign_discount_percent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='discount_percent',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
