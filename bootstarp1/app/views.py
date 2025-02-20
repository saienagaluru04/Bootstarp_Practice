from django.shortcuts import render

# Create your views here.
def cdn(request):
    return render(request,'cdn.html')

def button(request):
    return render(request,'button.html')

def buttontags(request):
    return render(request,'buttontags.html')

def outlineButtons(request):
    return render(request,'outlinebuttons.html')

def buttonSizes(request):
    return render(request,'buttonSizes.html')