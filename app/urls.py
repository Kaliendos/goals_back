from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from app.views import GoalViewSet, SubGoalViewSet

router = routers.SimpleRouter()

router.register('goals', GoalViewSet, basename="goals")
router.register(r'goals/(?P<goal_id>\d+)/sub_goals', SubGoalViewSet, basename="sub_goals")
urlpatterns = []
urlpatterns += router.urls