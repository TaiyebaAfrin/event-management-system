from django.urls import path
from tasks.views import manager_dashboard, participant_dashboard, create_task, event_list, dashboard, update_event, delete_event,view_event
# from tasks.views import base, manager_dashboard, participant_dashboard, create_task, ev_home, view_event, event_list, participants, update_event, category_list, delete_event, event_details, 
from django.views.generic import TemplateView
from .views import BaseView, CategoryListView, EventDetailView, ParticipantsView, EventHomeView



urlpatterns = [
    #path('base/', base),
    path('manager-dashboard/', manager_dashboard, name="manager-dashboard"),
    path('user-dashboard/', participant_dashboard),
    #path('home/', ev_home, name='home'),
    path('create-task/', create_task, name='create-task'),
    #path('event/<int:event_id>/details/', event_details, name='event-details'),
    path('view_event/', view_event, name='view_event'),
    path('event-list/', event_list, name='event_list'),
    #path('participants/', participants, name='participants'),
    #path('categories/', category_list, name='category_list'),
    path('update-event/<int:id>/', update_event, name='update-event'),
    path('delete-event/<int:id>/', delete_event, name='delete-event'),
    path('base/', BaseView.as_view(), name='base'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('event/<int:event_id>/', EventDetailView.as_view(), name='event_details'),
    path('event/<int:event_id>/details/', EventDetailView.as_view(), name='event-details'),
    path('participants/', ParticipantsView.as_view(), name='participants'),
    path('', EventHomeView.as_view(), name='event-home'), 
    path('dashboard/', dashboard, name='dashboard')




]


