# Generated by Django 4.2.18 on 2025-01-29 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markets_review', '0005_alter_review_stars_rating_ratings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='market',
            name='latitude',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='market',
            name='longitude',
            field=models.CharField(),
        ),
    ]
