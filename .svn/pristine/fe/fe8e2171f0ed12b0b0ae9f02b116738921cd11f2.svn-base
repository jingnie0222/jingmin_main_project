from django.urls import path
from .views import mission_list
from .views import mission_list_case
from .views import unsolved_case
from .views import unsolved_detail
from .views import mission_case_detail

app_name='lizhi_accu_compare'
urlpatterns = [
    path('mission_list/', mission_list, name='mission_list'),
    path('mission_list/unsolved_case/', unsolved_case, name='unsolved_case'),
    # path('unsolved_case/', unsolved_detail, name='unsolved_detail'),
    path('mission_list/<int:task_id>/', mission_list_case, name='case_list'),
    path('mission_list/<int:task_id>/<int:query_id>/', mission_case_detail, name='case_detail')
]