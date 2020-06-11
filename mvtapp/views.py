from django.shortcuts import render

# Create your views here.
def saran(request):
    return render(request,'saran.html')

def logi(request):
    return render(request,'logi.html')