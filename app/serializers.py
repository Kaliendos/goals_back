from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from app.models import Goal, SubGoal
from rest_framework.exceptions import APIException


class SubGoalSerializer(ModelSerializer):
    class Meta:
        model = SubGoal
        fields = ("id", "title", "deadline",)


class GoalSerializer(ModelSerializer):
    progress = serializers.SerializerMethodField()
   #  sub_goals = SubGoalSerializer(many=True, read_only=True)
    sub_goals = serializers.SerializerMethodField()
    class Meta:
        model = Goal
        fields = (
            "id", "title", "deadline", "reward", "max_value_to_achieve_goal",
            "managed_value", "progress", "sub_goals"
        )

    def get_progress(self, obj) -> int:
        if obj.max_value_to_achieve_goal == 0:
            return 0
        return round(obj.managed_value / obj.max_value_to_achieve_goal  * 100, 2)

    def get_sub_goals(self, ins):
        sub_goals = ins.sub_goals.order_by("deadline")
        return SubGoalSerializer(sub_goals,many=True).data


