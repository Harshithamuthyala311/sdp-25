# Generated by Django 5.0.1 on 2024-01-30 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propertyTitle', models.CharField(max_length=255)),
                ('propertyCost', models.CharField(max_length=255)),
                ('propertyType', models.CharField(choices=[('Residential', 'residential'), ('Commercial', 'commercial'), ('Industrial', 'industrial')], max_length=20)),
                ('benefits', models.TextField()),
                ('listing', models.CharField(max_length=255)),
                ('propertyLocation', models.CharField(max_length=255)),
                ('propertyRequirements', models.TextField()),
            ],
        ),
    ]
