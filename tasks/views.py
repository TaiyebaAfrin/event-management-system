from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import EventForm
from tasks.forms import EventForm, EventModelForm, EventDetailModelForm
from tasks.models import Participant, Event, Category
from datetime import date
from django.db.models import Q, Count, Max, Min, Avg
# Create your views here.

def base(request):
    return render(request, "events/base.html")

def manager_dashboard(request):
    # total_event = Event.objects.count() #TOTAL TASK
    # completed_event = Event.objects.filter(status= "COMPLETED").count #COMPLETED TASK
    # in_progress_event = Event.objects.filter(status= "IN_PROGRESS").count #TASK IN PROGRESS
    # pending_event = Event.objects.filter(status= "PENDING").count #todo

    counts = Event.objects.aggregate(
        total=Count('id'),
        completed=Count('id', filter=Q(status='COMPLETED')),
        in_progress=Count('id', filter=Q(status='IN_PROGRESS')),
        pending=Count('id', filter=Q(status='PENDING')),)
    # retrrvie
    base_query = Event.objects.select_related('details').prefetch_related('assigned_to')
    if type == 'completed':
        events = base_query.all()

    context = {
        'events': events,
        'counts': counts

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



def user_dashboard(request):
    return render(request, "events/user-dashboard.html")

def ev_home(request):
    return render(request, "events/home.html")


def event_list(request):
    events = Event.objects.all()
    return render(request, "events/event-list.html", {"events": events})
   



    


def test(request):
    names = ["Mahmud", "Ahamed", "John", "Mr. X"]
    count = 0
    for name in names:
        count += 1
    context = {
        "names": names,
        "age": 23,
        "count": count
    }
    return render(request, 'test.html', context)





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


def view_event(request):
    participants = Participant.objects.all()
    return render(request, "show_event.html", {"participants": participants})
    # categories = Category.objects.all()
    # categories = Category.objects.select_related()
    # return render(request, 'events/category_list.html', {'categories': categories})




def category_list(request):
    categories = Category.objects.all()
    return render(request, 'events/category_list.html', {'categories': categories})



# def view_event(request):
#     events = Event.objects.all()

#     event_5 = Event.objects.get(id=1)
#     return render(request, "show_event.html", {"events": events, "event5": event_5, })



# def create_task(request):
#     participants = Participant.objects.all()
    
#     if request.method == 'POST':
#         form = EventForm(request.POST, Participant=participants)
#         if form.is_valid():
#             event_data = form.cleaned_data
#             event = Event.objects.create(
#                 title=event_data['title'],
#                 description=event_data['description'],
#                 due_date=event_data['due_date']
#             )
#             event.assigned_to.set(event_data['assigned_to'])
#             return redirect('message')
#     else:
#         form = EventForm(Participant=participants)
    
#     return render(request, 'tasks/task_form.html', {"form": form, "message": "Event added successfully"})









