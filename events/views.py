
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Event
from cases.models import Case

@login_required
def events(request):
    upcoming_events = Event.objects.filter(date__gte=timezone.now()).order_by('date')
    past_events = Event.objects.filter(date__lt=timezone.now()).order_by('-date')
    return render(request, 'events.html', {
        'upcoming_events': upcoming_events,
        'past_events': past_events
    })

@login_required
def create_event(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        case_id = request.POST.get('case')
        event_type = request.POST.get('event_type')
        date = request.POST.get('date')
        location = request.POST.get('location', '')
        description = request.POST.get('description', '')
        
        case = get_object_or_404(Case, id=case_id)
        event = Event.objects.create(
            title=title,
            case=case,
            event_type=event_type,
            date=date,
            location=location,
            description=description
        )
        messages.success(request, f'Event "{title}" created successfully!')
        return redirect('events')
    
    cases = Case.objects.all()
    return render(request, 'create_event.html', {'cases': cases})

@login_required
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'event_detail.html', {'event': event})
