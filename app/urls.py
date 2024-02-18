from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.permissions import AllowAny

from app.views import GoalViewSet, SubGoalViewSet, is_user_exists

router = routers.SimpleRouter()
router.register('goals', GoalViewSet, basename="goals")
router.register(r'goals/(?P<goal_id>\d+)/sub_goals', SubGoalViewSet, basename="sub_goals")
urlpatterns = [path("check_user_exists/", is_user_exists)]
urlpatterns += router.urls
