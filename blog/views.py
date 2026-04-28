from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.text import slugify
from .models import Post, Category
from accounts.decorators import editor_required
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'content', 'image', 'excerpt', 'is_published']
        widgets = {'content': forms.Textarea(attrs={'rows': 10})}

def post_list(request):
    posts = Post.objects.filter(is_published=True)
    categories = Category.objects.all()
    cat = request.GET.get('category')
    if cat:
        posts = posts.filter(category__id=cat)
    return render(request, 'blog/post_list.html', {'posts': posts, 'categories': categories, 'selected_cat': cat})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, is_published=True)
    recent = Post.objects.filter(is_published=True).exclude(pk=post.pk)[:3]
    return render(request, 'blog/post_detail.html', {'post': post, 'recent': recent})

@login_required
@editor_required
def manage_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/manage_posts.html', {'posts': posts})

@login_required
@editor_required
def add_post(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.slug = slugify(post.title)
        post.save()
        messages.success(request, 'Post added.')
        return redirect('manage_posts')
    return render(request, 'blog/post_form.html', {'form': form, 'title': 'Add Post'})

@login_required
@editor_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, 'Post updated.')
        return redirect('manage_posts')
    return render(request, 'blog/post_form.html', {'form': form, 'title': 'Edit Post'})

@login_required
@editor_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted.')
        return redirect('manage_posts')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})
