# Generated by Django 5.1.6 on 2025-03-02 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(blank=True, null=True),
        ),
    ]
