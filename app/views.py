from django.shortcuts import render

# Create your views here.
d={'a':100,'b':50}
def hai(request):
    return render(request,'hai.html',d)