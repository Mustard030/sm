from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def timer(requset):
    import time
    context = dict()
    context['timer'] = time.time()
    return render(requset, 'timer.html', context=context)


def login(request):
    if request.method == 'GET':
        print(request.GET)
        return render(request, 'login.html')
    else:
        print(request.POST)
        return HttpResponse("ok")

