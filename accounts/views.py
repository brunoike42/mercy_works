import uuid
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Sum, Count
from .models import CustomUser
from .decorators import admin_required, editor_required
from causes.models import Cause
from events.models import Event
from donations.models import Donation, ContactSubmission
from volunteers.models import VolunteerApplication
from django import forms
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=20, required=False)
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'password1', 'password2']
    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'donor'
        user.is_email_verified = True
        if commit: user.save()
        return user


def register(request):
    if request.user.is_authenticated: return redirect('dashboard')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Welcome to Mercy Works!')
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated: return redirect('dashboard')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('dashboard')
        messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    user = request.user
    if user.role == 'admin':
        return redirect('admin_dashboard')
    elif user.role == 'editor':
        return redirect('editor_dashboard')
    else:
        return redirect('donor_dashboard')


@login_required
@admin_required
def admin_dashboard(request):
    stats = {
        'total_causes': Cause.objects.count(),
        'total_donations': Donation.objects.aggregate(total=Sum('amount'))['total'] or 0,
        'total_donors': CustomUser.objects.filter(role='donor').count(),
        'total_volunteers': VolunteerApplication.objects.filter(status='approved').count(),
        'pending_applications': VolunteerApplication.objects.filter(status='pending').count(),
        'unread_messages': ContactSubmission.objects.filter(is_read=False).count(),
        'total_events': Event.objects.count(),
    }
    recent_donations = Donation.objects.order_by('-created_at')[:5]
    recent_applications = VolunteerApplication.objects.order_by('-created_at')[:5]
    return render(request, 'accounts/admin_dashboard.html', {
        'stats': stats,
        'recent_donations': recent_donations,
        'recent_applications': recent_applications,
    })


@login_required
@editor_required
def editor_dashboard(request):
    from blog.models import Post
    stats = {
        'my_posts': Post.objects.filter(author=request.user).count(),
        'total_causes': Cause.objects.count(),
        'upcoming_events': Event.objects.count(),
    }
    return render(request, 'accounts/editor_dashboard.html', {'stats': stats})


@login_required
def donor_dashboard(request):
    my_donations = Donation.objects.filter(donor=request.user).order_by('-created_at')
    my_applications = VolunteerApplication.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'accounts/donor_dashboard.html', {
        'my_donations': my_donations,
        'my_applications': my_applications,
        'total_donated': my_donations.aggregate(total=Sum('amount'))['total'] or 0,
    })


@login_required
@admin_required
def manage_users(request):
    users = CustomUser.objects.all().order_by('-date_joined')
    return render(request, 'accounts/manage_users.html', {'users': users})


@login_required
@admin_required
def toggle_user_status(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    user.is_active = not user.is_active
    user.save()
    messages.success(request, f'User {"activated" if user.is_active else "deactivated"}.')
    return redirect('manage_users')


@login_required
@admin_required
def change_user_role(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        new_role = request.POST.get('role')
        if new_role in dict(CustomUser.ROLE_CHOICES):
            user.role = new_role
            user.save()
            messages.success(request, f'Role updated to {new_role}.')
    return redirect('manage_users')


def access_denied(request):
    return render(request, 'accounts/access_denied.html', status=403)
