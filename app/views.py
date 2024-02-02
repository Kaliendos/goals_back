from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from app.models import Goal, SubGoal
from app.permissions import IsOwner
from app.serializers import GoalSerializer, SubGoalSerializer


class GoalViewSet(ModelViewSet):
    serializer_class = GoalSerializer
    permission_classes = (IsAuthenticated,IsOwner)

    def get_queryset(self):
        user = self.request.user
        return user.goals

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class SubGoalViewSet(ModelViewSet):
    serializer_class = SubGoalSerializer
    permission_classes = (IsAuthenticated, )

    def get_retrieve_goal(self):
        return get_object_or_404(Goal, id=self.kwargs.get("goal_id"))

    def get_queryset(self):
        retrieve_goal = self.get_retrieve_goal()
        return retrieve_goal.sub_goals


    def perform_create(self, serializer):
        serializer.save(goal=self.get_retrieve_goal())


