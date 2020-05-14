from django.shortcuts import render


def explore(request):
    return render(request, "index-style1.html")

# def products(request):
#     return render(request, 'products.html')
