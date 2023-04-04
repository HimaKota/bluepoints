from django.http import HttpResponse

def home(request):
   return HttpResponse('<h1>welcome to my app !</h1>')