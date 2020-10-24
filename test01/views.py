from django.shortcuts import render
from templates import *


# Create your views here.
def timer(requset):
    import time
    context = {'time': time.time()}
    return render(requset, template_name='timer.html', context=context)
