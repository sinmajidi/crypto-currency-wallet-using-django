from django.shortcuts import render,HttpResponseRedirect,HttpResponse,redirect
from rest_framework.response import Response
from rest_framework.decorators import APIView

class Index(APIView):
    def get(self, request):
        if request.COOKIES and 'user' in request.COOKIES and request.COOKIES['user']:
            return render(request, 'greating/index.html',context={"login":True})
        else:
            return redirect('/user/login')


class About(APIView):
    def get(self, request):
        return render(request, 'greating/about.html')