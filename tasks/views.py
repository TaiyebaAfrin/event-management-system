from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import EventForm
from tasks.forms import EventForm, EventModelForm
from tasks.models import Participant, Event
from datetime import date
from django.db.models import Q, Count, Max, Min, Avg
# Create your views here.

def base(request):
    return render(request, "events/base.html")

def manager_dashboard(request):
    return render(request, "events/manager-dashboard.html")



def user_dashboard(request):
    return render(request, "events/user-dashboard.html")

# def ev_home(request):
#     return render(request, "events/home.html")
   
def ev_home(request):
    event_3 = Event.objects.get(id=1)
    event_2 = Event.objects.get(id=2)
    return render(request, "events/home.html", {
        "event3": event_3,
        "event2": event_2
    })


    


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
    participants = Participant.objects.all()
    form = EventModelForm()
    if request.method == "POST":
        form = EventForm(request.POST, Participant=participants)
        if form.is_valid():
            form.save()
            
        return render(request, 'task_form.html', {"form": form, "message": "task added successfully"})
           

    context = {"form": form}
    return render(request, "task_form.html", context)



def view_event(request):
    events = Event.objects.all()

    event_5 = Event.objects.get(id=1)
    return render(request, "show_event.html", {"events": events, "event5": event_5, })



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









