# Generated by Django 4.2.17 on 2025-03-12 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('markets_review', '0013_remove_market_review_rating'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Ratings',
        ),
    ]
