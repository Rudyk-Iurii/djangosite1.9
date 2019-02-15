from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .models import Post
from .forms import PostForm
# Create your views here.


def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print (form.cleaned_data.get("title"))
        instance.save()
        # message success
        messages.success(request, "Successfully created")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "form": form,
    }
    return render(request, 'post_form.html', context)


def post_detail(request, id = None, ):
    # instance = Post.objects.get(id=8)
    instance = get_object_or_404(Post, id = id)

    context = {
        "title": instance.title,
        "instance": instance
    }
    return render(request, 'post_detail.html', context)

def post_list(request):
    queryset = Post.objects.all()
    context = {
        "title": "List",
        "object_list": queryset
        }
   # проверка на логин
    #     } # if request.user.is_authenticated():
    #     #     context = {
    #     #     "title": "My User List"
    #     #     }
    #     # else:
    #     #     context = {
    #     #     "title": "List"

    return render (request, 'index.html', context)
    # return HttpResponse("<h1>List</h1>")


def post_update(request, id = None):
    instance = get_object_or_404(Post, id = id)
    form = PostForm(request.POST or None, instance = instance) # последнее позволяет заполнить поля
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #message success
        messages.success(request, "Successfully saved", extra_tags='some-tags')
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }

    return render(request, 'post_form.html', context)


def post_delete(request, id = None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect("posts:list")