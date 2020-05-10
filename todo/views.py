from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponseRedirect , HttpResponse
from todo.models import TodoItem
from django.urls import reverse


def todo_view(request) :
    all_to_do_items = TodoItem.objects.all()
    return render(request,"todo.html",{"all_items": all_to_do_items})

def addTodo(request) :
    if request.is_ajax and request.method == "POST":
        new_item = TodoItem(content = request.POST['content'])
        new_item.save()
        ser_instance = serializers.serialize('json', [ new_item, ])
        return JsonResponse({"new_item": ser_instance}, status=200)
    else :
         return JsonResponse({"error": new_item.errors}, status=400)

def deleteTodo(request) :
    if request.is_ajax and request.method == "POST":
        item = TodoItem.objects.get(id=request.POST.get('id'))
        item.delete()
    else :
        return JsonResponse({"error": item.errors}, status=400)
    return HttpResponseRedirect('/todo/')

def updateTodo(request) :
    item = TodoItem.objects.get(id=request.POST.get('id'))
    item.content = request.POST['content']
    item.save()
    return HttpResponseRedirect('/todo/')


