from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Donation, ContactSubmission
from causes.models import Cause
from accounts.decorators import admin_required
from django import forms

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['cause', 'donor_name', 'donor_email', 'amount', 'message', 'is_anonymous']

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'subject', 'message']

def donate(request, cause_id=None):
    cause = None
    if cause_id:
        cause = get_object_or_404(Cause, pk=cause_id)
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            if request.user.is_authenticated:
                donation.donor = request.user
            donation.save()
            messages.success(request, f'Thank you for your donation of UGX {donation.amount}! God bless you.')
            return redirect('cause_list')
    else:
        initial = {'cause': cause} if cause else {}
        if request.user.is_authenticated:
            initial['donor_name'] = request.user.get_full_name() or request.user.username
            initial['donor_email'] = request.user.email
        form = DonationForm(initial=initial)
    return render(request, 'donations/donate.html', {'form': form, 'cause': cause})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message sent! We will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'donations/contact.html', {'form': form})

@login_required
@admin_required
def manage_donations(request):
    donations = Donation.objects.all().order_by('-created_at')
    return render(request, 'donations/manage_donations.html', {'donations': donations})

@login_required
@admin_required
def manage_messages(request):
    messages_qs = ContactSubmission.objects.all()
    return render(request, 'donations/manage_messages.html', {'messages': messages_qs})

@login_required
@admin_required
def mark_message_read(request, pk):
    msg = get_object_or_404(ContactSubmission, pk=pk)
    msg.is_read = True
    msg.save()
    return redirect('manage_messages')
