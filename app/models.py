import datetime

from django.contrib.auth import get_user_model
from django.db import models

USER = get_user_model()


class Goal(models.Model):
    author = models.ForeignKey(
        USER,
        on_delete=models.CASCADE,
        related_name="goals"
    )
    title = models.CharField(max_length=255)
    deadline = models.DateTimeField(default=datetime.datetime.now())
    measurable = models.CharField(max_length=255)
    max_value_to_achieve_goal = models.PositiveIntegerField(default=0)
    managed_value = models.PositiveIntegerField(default=0)  # Текущий прогресс пользователя
    relevant = models.CharField(max_length=255, blank=True, null=True)
    is_done = models.BooleanField(default=False)


class SubGoal(models.Model):
    title = models.CharField(max_length=255)
    deadline = models.DateTimeField(default=datetime.datetime.now())
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name="sub_goals")
    is_done = models.BooleanField(default=False)



