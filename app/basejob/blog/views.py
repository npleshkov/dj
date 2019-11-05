from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def posts_list(request):
    #return HttpResponse('<h1>Hello word</h1>')
    n = ['Oleg', 'Masha', 'Olga']
    return render(request, 'blog/index.html', context = {'names': n})