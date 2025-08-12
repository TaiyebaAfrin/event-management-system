from django.shortcuts import render, redirect
from django.http import HttpResponse
from tasks.forms import EventForm, EventModelForm, EventDetailModelForm
from tasks.models import Participant, Event, Category
from datetime import date
from django.db.models import Q, Count, Max, Min, Avg
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required, permission_required


# Create your views here.
def is_manager(user):
    return user.groups.filter(name='Manager').exists()

def is_participant(user):
    return user.groups.filter(name='Manager').exists()





def base(request):
    return render(request, "events/base.html")

#@user_passes_test(is_manager, login_url='no-permission')
def manager_dashboard(request):
    events = Event.objects.select_related('details').prefetch_related('assigned_to')
    counts = Event.objects.aggregate(
        total=Count('id'),
        completed=Count('id', filter=Q(status='COMPLETED')),
        in_progress=Count('id', filter=Q(status='IN_PROGRESS')),
        pending=Count('id', filter=Q(status='PENDING')),)
    # retrrvie
    base_query = Event.objects.select_related('details').prefetch_related('assigned_to')


    type = request.GET.get('type', 'all')

    if type == 'completed':
        events = base_query.filter(status= "COMPLETED")
    elif type == 'in-progress':
        events = base_query.filter(status='IN_PROGRESS')
    elif type == 'pending':
        events = base_query.filter(status='PENDING')
    elif type == 'all':
        events = base_query.all()

    context = {
        'events': events,
        'counts': counts,
        'role': 'organizer' #manager

    }
    return render(request, "events/manager-dashboard.html", context)
    # context = {
    #    "events": events,
    #    "total_event": total_event,
    #    "completed_event": completed_event,
    #    "pending_event": pending_event,
    #    "in_progress_event": in_progress_event

    # }
    #return render(request, "events/manager-dashboard.html", context)


#@user_passes_test(is_participant, login_url='no-permission')
def participant_dashboard(request):
    return render(request, "events/user-dashboard.html")

def ev_home(request):
    return render(request, "events/home.html")


def event_list(request):
    events = Event.objects.all()
    return render(request, "events/event-list.html", {"events": events})
   


#@login_required
#@permission_required("tasks.add_event", login_url='no-permission')
def create_task(request):
    #participants = Participant.objects.all()
    event_form = EventModelForm()
    event_detail_form = EventDetailModelForm()
    
    if request.method == "POST":
        event_form = EventModelForm(request.POST)
        event_detail_form = EventDetailModelForm(request.POST)
        

        if event_form.is_valid and event_detail_form.is_valid():
            event = event_form.save()
            event_detail = event_detail_form.save(commit=False)
            event_detail.event = event
            event_detail.save()
            
            messages.success(request, "Event added successfully")
            return redirect('create-task')
           

    context = {"event_form": event_form, "event_detail_form": event_detail_form}
    return render(request, "task_form.html", context)


@login_required
#@permission_required("tasks.change_event", login_url='no-permission')

def update_event(request, id):
    event = Event.objects.get(id=id)
    event_form = EventModelForm(instance=event)

    if event.details:
       event_detail_form = EventDetailModelForm(instance=event.details)
    
    if request.method == "POST":
        event_form = EventModelForm(request.POST, instance=event)
        event_detail_form = EventDetailModelForm(request.POST, instance=event.details)
        

        if event_form.is_valid and event_detail_form.is_valid():
            event_form = event_form.save()
            # event_detail = event_detail_form.save(commit=False)
            # event_detail.event = event
            event_detail_form.save()
            
            messages.success(request, "Event Updated successfully")
            return redirect('update-event', id)
           

    context = {"event_form": event_form, "event_detail_form": event_detail_form}
    return render(request, "task_form.html", context)



@login_required
#@permission_required("tasks.delete_event", login_url='no-permission')
def delete_event(request, id):
    if request.method == 'POST':
        event = Event.objects.get(id=id)
        event.delete()
        messages.success(request, 'Event Deleted Successfully')
        return redirect('manager-dashboard')
    else:
        messages.error(request, 'Something went wrong')
        return redirect('manager-dashboard')











def participants(request):
     participants = Participant.objects.all()
     return render(request, "events/participants.html", {"participants": participants})

@login_required
#@permission_required("tasks.view_event", login_url='no-permission')
def view_event(request):
    participants = Participant.objects.all(
        num_event=Count('events')).order_by('num_event')
    return render(request, "show_event.html", {"participants": participants})
    # categories = Category.objects.all()
    # categories = Category.objects.select_related()
    # return render(request, 'events/category_list.html', {'categories': categories})




def category_list(request):
    categories = Category.objects.all()
    return render(request, 'events/category_list.html', {'categories': categories})


@login_required
#@permission_required("tasks.view_event", login_url='no-permission')
def event_details(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'events/event_details.html',{"event": event})