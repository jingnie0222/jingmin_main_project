from django.urls import path
from .views import monitor_list
from .views import monitor_item_detail
from .views import notice_receive
from .views import page

app_name = 'monitor_notice'
urlpatterns = [
    path('notice_list/', monitor_list, name='notice_list'),
    # path('mission_list/<int:task_id>/', mission_list_case, name='case_list'),
    path('notice_list/<int:id>/', monitor_item_detail, name='notice_item_detail'),
    path('notice_receive/', notice_receive),
    path('page/', page, name='notice_page'),
]
