from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.
def add_post(request):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            redirect("add_post")
            post_form.save()
    else:
        post_form = forms.PostForm()
    return render(request,'add_post.html',{"form":post_form})

def edit_post(request, id):
    post = models.Post.objects.get(pk = id)
    # print(post.title)
    post_form = forms.PostForm(instance=post)


    if request.method == 'POST':
        post_form = forms.PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect("homepage")
    
    return render(request,'add_post.html',{"form":post_form})


def delete_post(request, id):
    post = models.Post.objects.get(pk = id)
    post.delete()
    return redirect('homepage')