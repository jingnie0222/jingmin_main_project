from django.urls import path
from .views import mission_list, mission_add

urlpatterns = [
    path('mission_list/', mission_list),
    path('mission_add/', mission_add),
]
