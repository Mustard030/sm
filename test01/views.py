from django.shortcuts import render


# Create your views here.
def timer(requset):
    import time
    context = dict()
    context['time'] = time.time()
    return render(requset, 'timer.html', context=context)
