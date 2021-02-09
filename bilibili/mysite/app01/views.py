from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
	return HttpResponse("Hello Django")
	pass

def login(request):
	return render(request, 'login.html')
	pass