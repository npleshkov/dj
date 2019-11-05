from django.shortcuts import render

# Create your views here.
# Create your views here.
def candidate_list(request):
    #return HttpResponse('<h1>Hello word</h1>')
    n = ['Oleg', 'Masha', 'Olga']
    return render(request, 'candidate/index.html', context = {'names': n})