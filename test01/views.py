from django.shortcuts import render


# Create your views here.
def timer(requset):
    import time
    context = dict()
    context['timer'] = time.time()
    return render(requset, 'timer.html', context=context)
