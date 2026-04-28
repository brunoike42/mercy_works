from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Cause
from accounts.decorators import editor_required
from django import forms

class CauseForm(forms.ModelForm):
    class Meta:
        model = Cause
        fields = ['title', 'description', 'image', 'goal_amount', 'is_active', 'is_featured']

def cause_list(request):
    causes = Cause.objects.filter(is_active=True)
    return render(request, 'causes/cause_list.html', {'causes': causes})

def cause_detail(request, pk):
    cause = get_object_or_404(Cause, pk=pk, is_active=True)
    return render(request, 'causes/cause_detail.html', {'cause': cause})

@login_required
@editor_required
def manage_causes(request):
    causes = Cause.objects.all()
    return render(request, 'causes/manage_causes.html', {'causes': causes})

@login_required
@editor_required
def add_cause(request):
    form = CauseForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Cause added.')
        return redirect('manage_causes')
    return render(request, 'causes/cause_form.html', {'form': form, 'title': 'Add Cause'})

@login_required
@editor_required
def edit_cause(request, pk):
    cause = get_object_or_404(Cause, pk=pk)
    form = CauseForm(request.POST or None, request.FILES or None, instance=cause)
    if form.is_valid():
        form.save()
        messages.success(request, 'Cause updated.')
        return redirect('manage_causes')
    return render(request, 'causes/cause_form.html', {'form': form, 'title': 'Edit Cause', 'cause': cause})

@login_required
@editor_required
def delete_cause(request, pk):
    cause = get_object_or_404(Cause, pk=pk)
    if request.method == 'POST':
        cause.delete()
        messages.success(request, 'Cause deleted.')
        return redirect('manage_causes')
    return render(request, 'causes/cause_confirm_delete.html', {'cause': cause})
