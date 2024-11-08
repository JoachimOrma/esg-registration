# Generated by Django 5.1.2 on 2024-11-03 07:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mentee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.CharField(max_length=5)),
                ('current_education', models.CharField(max_length=255)),
                ('career_path', models.CharField(max_length=255)),
                ('industry_interest', models.CharField(max_length=255)),
                ('desired_skill', models.TextField()),
                ('availability', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['first_name', 'last_name'],
            },
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.CharField(max_length=5)),
                ('current_position', models.CharField(max_length=255)),
                ('current_industry', models.CharField(max_length=255)),
                ('previous_industry_exp', models.TextField()),
                ('areas_of_expertise', models.TextField()),
                ('availability', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['first_name', 'last_name'],
            },
        ),
    ]
