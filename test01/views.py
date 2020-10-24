from django.shortcuts import render


# Create your views here.
def timer(requset):
    import time
    context = dict()
    context['timer'] = 123
    return render(requset, 'timer.html', context=context)
