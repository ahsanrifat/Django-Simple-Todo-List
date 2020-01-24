from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from todoApp.models import TodoItem

# Create your views here.
def todoView(request):
    items=TodoItem.objects.all()
    #return HttpResponse('Hello, this is todo view')
    return render(request,'todo.html',{'all':items})

def addItem(request):
    #create a new todo item
    #save
    #redirect user to the original page

    new=request.POST['content']
    #new="New Added Item"
    new_item=TodoItem(content=new)
    new_item.save()
    return HttpResponseRedirect('/todo/')


def removeItem(request, itemId):
    toBeDeleted=TodoItem.objects.get(id=itemId)
    toBeDeleted.delete()
    return HttpResponseRedirect('/todo/')    