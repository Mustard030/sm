from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.urls import reverse

# Create your views here.
def timer(requset):
    import time
    context = dict()
    context['timer'] = time.time()
    return render(requset, 'timer.html', context=context)

def index(request):
    return HttpResponse(reverse("test01:index"))

def login(request):
    print(reverse('test01:Log'))
    if request.method == 'GET':
        print(request.GET)
        return render(request, 'login.html')
    else:
        print(request.POST)
        return HttpResponse("OK")

