from django.shortcuts import render,HttpResponse,redirect
from rest_framework.response import Response
from rest_framework.decorators import APIView
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from bitcoinaddress import Wallet
import jwt
import datetime
from expansion.settings import SECRET_KEY
import qrcode
class Signin(APIView):
    def get(self, request):
        return render(request, 'user/signin.html')
    def post(self, request):
        user=User.objects.filter(username=request.data['username']).first()
        if not user:
            user = User.objects.filter(email=request.data['username']).first()
            if not user:
                return redirect('/user/login')
        if check_password_hash(user.password, request.data['password']):
            token = jwt.encode(
                {'email': user.email, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60)},
                SECRET_KEY)
            response = redirect('/')
            response.set_cookie('user', token.decode("utf-8"))
            return response

        else:
            return redirect('/about')

class Signup(APIView):
    def get(self, request):
        return render(request, 'user/signin.html')
    def post(self, request):
        if request.data['password']==request.data['re-password']:
            wallet = Wallet()
            private_key = wallet.key.__dict__['hex']
            public_key = wallet.address.__dict__['pubkey']
            public_address = wallet.address.__dict__['mainnet'].pubaddr1
            hashed_password = generate_password_hash(request.data['password'], method='sha256')
            user=User(username=request.data['username'],email=request.data['email'],password=hashed_password,
                      is_enable=True,is_confrimed=False,public_address=public_address,private_key=private_key,
                  public_key=public_key,asset=0,profit=0)
            user.save()
            data = public_address
            img = qrcode.make(data)
            # img.save('/absolute/path/to/myphoto.jpg', 'JPEG')
            img.save('static/qr/'+request.data['username']+'.png')
            return redirect('/')
        else:
            pass
            return redirect('/user/login')

class User_info(APIView):
    def get(self, request):
        users = User.objects.all()
        return HttpResponse(users)

class Logout(APIView):
    def get(self, request):
        if request.COOKIES['user']:
            response = redirect('/')
            response.delete_cookie('user')
            return response
        else:
            return redirect('/')
class start_invesment(APIView):
    def get(self, request):
        if request.COOKIES['user']:
            token=request.COOKIES['user']
            try:
                data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            except:
                response = redirect('/user/login')
                response.delete_cookie('user')
                return response
            current_user = User.objects.filter(email=data['email']).first()
            if not current_user:
                return redirect('/user/login')
            context={"public_address":current_user.public_address,'username':current_user.username,'login':True}
            return render(request, 'wallet/wallet.html',context=context)

        else:
            return redirect('/')