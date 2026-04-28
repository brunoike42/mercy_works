from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import VolunteerOpportunity, VolunteerApplication
from accounts.decorators import admin_required, editor_required
from django import forms

class OpportunityForm(forms.ModelForm):
    class Meta:
        model = VolunteerOpportunity
        fields = ['title', 'description', 'requirements', 'location', 'is_active']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = VolunteerApplication
        fields = ['name', 'email', 'phone', 'message']

def opportunity_list(request):
    opportunities = VolunteerOpportunity.objects.filter(is_active=True)
    return render(request, 'volunteers/opportunity_list.html', {'opportunities': opportunities})

def apply(request, pk):
    opportunity = get_object_or_404(VolunteerOpportunity, pk=pk, is_active=True)
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            app = form.save(commit=False)
            app.opportunity = opportunity
            if request.user.is_authenticated:
                app.user = request.user
            app.save()
            messages.success(request, 'Application submitted! We will contact you soon.')
            return redirect('opportunity_list')
    else:
        initial = {}
        if request.user.is_authenticated:
            initial = {'name': request.user.get_full_name(), 'email': request.user.email, 'phone': request.user.phone}
        form = ApplicationForm(initial=initial)
    return render(request, 'volunteers/apply.html', {'form': form, 'opportunity': opportunity})

@login_required
@admin_required
def manage_opportunities(request):
    opportunities = VolunteerOpportunity.objects.all()
    return render(request, 'volunteers/manage_opportunities.html', {'opportunities': opportunities})

@login_required
@admin_required
def add_opportunity(request):
    form = OpportunityForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Opportunity added.')
        return redirect('manage_opportunities')
    return render(request, 'volunteers/opportunity_form.html', {'form': form, 'title': 'Add Opportunity'})

@login_required
@admin_required
def edit_opportunity(request, pk):
    opp = get_object_or_404(VolunteerOpportunity, pk=pk)
    form = OpportunityForm(request.POST or None, instance=opp)
    if form.is_valid():
        form.save()
        messages.success(request, 'Opportunity updated.')
        return redirect('manage_opportunities')
    return render(request, 'volunteers/opportunity_form.html', {'form': form, 'title': 'Edit Opportunity'})

@login_required
@admin_required
def manage_applications(request):
    applications = VolunteerApplication.objects.all()
    return render(request, 'volunteers/manage_applications.html', {'applications': applications})

@login_required
@admin_required
def update_application_status(request, pk):
    app = get_object_or_404(VolunteerApplication, pk=pk)
    if request.method == 'POST':
        app.status = request.POST.get('status', 'pending')
        app.save()
        messages.success(request, 'Application status updated.')
    return redirect('manage_applications')
