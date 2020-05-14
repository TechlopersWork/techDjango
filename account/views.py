from django.shortcuts import render

# Create your views here.
def techlopian(request):
    return render(request, 'techlopian.html')

def client(request):
    return render(request, 'client.html')