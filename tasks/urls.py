from django.urls import path
from tasks.views import base, manager_dashboard, participant_dashboard, create_task, ev_home, view_event, event_list, participants, update_event, category_list, delete_event


urlpatterns = [
    path('base/', base),
    path('manager-dashboard/', manager_dashboard, name="manager-dashboard"),
    path('user-dashboard/', participant_dashboard),
    path('home/', ev_home, name='home'),
    path('create-task/', create_task, name='create-task'),
    path('view_event/', view_event, name='view_event'),
    path('event-list/', event_list, name='event_list'),
    path('participants/', participants, name='participants'),
    path('categories/', category_list, name='category_list'),
    path('update-event/<int:id>/', update_event, name='update-event'),
    path('delete-event/<int:id>/', delete_event, name='delete-event'),
]


