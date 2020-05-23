from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse

from .models import BlogPost, Entry
from .forms import BlogPostForm, EntryForm

# Create your views here.

def index(request):
    """The home page for blogs."""
    return render(request, 'blogs/index.html')


@login_required
def blogposts(request):
    """Show all the blogposts."""
    blogposts = BlogPost.objects.filter(owner=request.user).order_by('-date_added')
    context = {'blogposts': blogposts}
    return render(request, 'blogs/blogposts.html', context)


@login_required
def blogpost(request, blogpost_id):
    """Show a particular blogpost and display its contents."""
    blogpost = BlogPost.objects.get(id=blogpost_id)

    # Make sure the blogpost belongs to the current user.
    if blogpost.owner != request.user:
        raise Http404

    entries = blogpost.entry_set.order_by('-date_added')
    context = {'blogpost': blogpost, 'entries': entries}
    return render(request, 'blogs/blogpost.html', context)


@login_required
def new_blogpost(request):
    """Add a new blogpost."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BlogPostForm()

    else:
        # POST data submitted; process data.
        form = BlogPostForm(request.POST)
        if form.is_valid():
            new_blogpost = form.save(commit=False)
            new_blogpost.owner = request.user
            new_blogpost.save()
            return HttpResponseRedirect(reverse('blogs:blogposts'))

    context = {'form': form}
    return render(request, 'blogs/new_blogpost.html', context)


@login_required
def new_entry(request, blogpost_id):
    """Add new content for a particular blogpost."""
    blogpost = BlogPost.objects.get(id=blogpost_id)
    if blogpost.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()

    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.blogpost = blogpost
            new_entry.save()
            return HttpResponseRedirect(reverse('blogs:blogpost', args=[blogpost_id]))

    context = {'blogpost': blogpost, 'form': form}
    return render(request, 'blogs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry or conten."""
    entry = Entry.objects.get(id=entry_id)
    blogpost = entry.blogpost
    if blogpost.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current content.
        form = EntryForm(instance=entry)

    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            new_blogpost = form.save(commit=False)
            new_blogpost.owner = request.user
            new_blogpost.save()
            form.save()
            return HttpResponseRedirect(reverse('blogs:blogpost', args=[blogpost.id]))

    context = {'entry': entry, 'blogpost': blogpost, 'form': form}
    return render(request, 'blogs/edit_entry.html', context)



