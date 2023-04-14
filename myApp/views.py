from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages,auth
from .models import Users


def home(request):
   if request.user.is_authenticated:
      current_user=request.user
      user_id=current_user.email   
      res= Users.objects.all().filter(EMAIL_ID=user_id,UESR_STUS=True)
      context = {
            'results': res,
      }
      return render(request,'home.html',context)
   else:
      return render(request,'index.html')
   

@login_required(login_url='login')
def logout(request):
   auth.logout(request) 
   messages.success(request, 'You are Logged out')
   return redirect('home')