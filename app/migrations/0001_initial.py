# Generated by Django 5.0.1 on 2024-01-17 16:04

import datetime
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
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('deadline', models.DateTimeField(default=datetime.datetime(2024, 1, 17, 16, 4, 24, 48385))),
                ('reward', models.CharField(max_length=255)),
                ('max_value_to_achieve_goal', models.PositiveIntegerField(default=0)),
                ('managed_value', models.PositiveIntegerField(default=0)),
                ('progress', models.PositiveSmallIntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goals', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubGoal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('deadline', models.DateTimeField(default=datetime.datetime(2024, 1, 17, 16, 4, 24, 49213))),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_goals', to='app.goal')),
            ],
        ),
    ]
