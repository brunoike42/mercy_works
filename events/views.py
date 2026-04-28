from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event
from accounts.decorators import editor_required
from django import forms

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'image', 'date', 'time', 'location', 'is_active']
        widgets = {'date': forms.DateInput(attrs={'type': 'date'}), 'time': forms.TimeInput(attrs={'type': 'time'})}

def event_list(request):
    events = Event.objects.filter(is_active=True)
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/event_detail.html', {'event': event})

@login_required
@editor_required
def manage_events(request):
    events = Event.objects.all()
    return render(request, 'events/manage_events.html', {'events': events})

@login_required
@editor_required
def add_event(request):
    form = EventForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Event added.')
        return redirect('manage_events')
    return render(request, 'events/event_form.html', {'form': form, 'title': 'Add Event'})

@login_required
@editor_required
def edit_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    form = EventForm(request.POST or None, request.FILES or None, instance=event)
    if form.is_valid():
        form.save()
        messages.success(request, 'Event updated.')
        return redirect('manage_events')
    return render(request, 'events/event_form.html', {'form': form, 'title': 'Edit Event'})

@login_required
@editor_required
def delete_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Event deleted.')
        return redirect('manage_events')
    return render(request, 'events/event_confirm_delete.html', {'event': event})
