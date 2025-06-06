# Generated by Django 5.0.7 on 2025-05-13 14:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matric_number', models.CharField(max_length=20, unique=True)),
                ('full_name', models.CharField(max_length=100)),
                ('project_topic', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('introduction', models.PositiveIntegerField()),
                ('problem_statement', models.PositiveIntegerField()),
                ('objectives', models.PositiveIntegerField()),
                ('methodology', models.PositiveIntegerField()),
                ('architecture', models.PositiveIntegerField()),
                ('significance', models.PositiveIntegerField()),
                ('related_works', models.PositiveIntegerField()),
                ('design_analysis', models.PositiveIntegerField()),
                ('implementation', models.PositiveIntegerField()),
                ('total_score', models.PositiveIntegerField(editable=False)),
                ('evaluator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='score.student')),
            ],
            options={
                'unique_together': {('evaluator', 'student')},
            },
        ),
    ]
