from django.urls import path
from tasks.views import base, manager_dashboard, user_dashboard, create_task, ev_home, test, view_event


urlpatterns = [
    path('base/', base),
    path('manager-dashboard/', manager_dashboard, name="manager-dashboard"),
    path('user-dashboard/', user_dashboard),
    path('home/', ev_home, name='home'),
    path('create-task/', create_task, name='create-task'),
    path('test/', test),
    path('view_event/', view_event, name='view_event'),
]


