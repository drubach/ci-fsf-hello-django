'''Views functions'''
#from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def get_todo_list(request):
    '''Get todo list'''
    return render(request, 'todo/todo_list.html')
