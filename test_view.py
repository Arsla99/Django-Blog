from django.http import HttpResponse
from django.shortcuts import render

def test_view(request):
    return HttpResponse("<h1>Django is Working!</h1><p>If you see this, the server is running correctly.</p>")
