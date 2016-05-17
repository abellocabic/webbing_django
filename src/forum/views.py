from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect

from .models import Post, Comment
from .forms import CommentForm

# Create your views here.

def forum_list(request):
	queryset = Post.objects.all()
	context = {
		'title' : 'Forum Marcus et Ginette',
		'object_list' : queryset,
	}
	return render(request, "forum_list.html", context)

def forum_detail(request, id):
	instance = get_object_or_404(Post, id=id)
	
	form = CommentForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
	
	context = {
		'title' : instance.title,
		'instance' : instance,
		'form' : form,
	}
	return render(request, "forum_detail.html", context)

def home_show(request) :
	context = {
		'title' : 'Marcus et Ginette',
	}
	return render(request, 'home.html', context)

