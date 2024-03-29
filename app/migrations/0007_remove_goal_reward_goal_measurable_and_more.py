# Generated by Django 5.0.1 on 2024-02-14 14:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_subgoal_is_done_alter_goal_deadline_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goal',
            name='reward',
        ),
        migrations.AddField(
            model_name='goal',
            name='measurable',
            field=models.CharField(default='1', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='goal',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 14, 17, 25, 53, 908922)),
        ),
        migrations.AlterField(
            model_name='subgoal',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 14, 17, 25, 53, 909921)),
        ),
    ]
