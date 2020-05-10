from django.shortcuts import render
from django.http import HttpResponseRedirect , HttpResponse
from todo.models import TodoItem


def todo_view(request) :
    all_to_do_items = TodoItem.objects.all()
    return render(request,"todo.html",{"all_items": all_to_do_items})

def addTodo(request) :
    new_item = TodoItem(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')

def deleteTodo(request) :
    item = TodoItem.objects.get(id=request.POST.get('id'))
    item.delete()
    return HttpResponseRedirect('/todo/')
