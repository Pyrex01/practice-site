import json
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import get_user_model
from django.http import JsonResponse
import random
from POSTs.models import Post
# Create your views here.
User = get_user_model()


def index(request):
    post = Post.objects.all()
    args = {
        "post":post
    }
    return render(request,"index.html",args)


def login(request):
    if request.method == 'GET':
        return render(request,"login.html")
    if request.method == 'POST' and request.is_ajax():
        number = request.POST["number"]
        password = request.POST["password"]
        user = auth.authenticate(phone_no=number,password=password)
        if user is not None:
            auth.login(request,user)
            data = {
                "status":"1",
                "msg":"/"
            }
            return JsonResponse(data)
        else:
            data = {
                "status":"0",
                "msg":"wrong username or password"
            }
            return JsonResponse(data)



def signup(request):
    if request.method == 'GET':
        return render(request,"signup.html")
    if request.method == 'POST' and request.is_ajax():
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        date_of_birth = request.POST["date_birth"]
        password = request.POST["password"]
        email = request.POST["email"]
        Phone_number = request.POST["number"]
        gender = request.POST["gender"]
        user = User.objects.create_user(
            password=password,
            email=email,
            phone_no=Phone_number,
            date_of_birth=date_of_birth,
            first_name=first_name,
            last_name=last_name,
            gender=gender
        )
        user.save()
        data = {
            "status":"1",
            "msg":"login"
        }
        return JsonResponse(data)


def send_otp(request):
    if request.method == 'POST' and request.is_ajax():
        num = request.POST["number"]
        if User.objects.filter(phone_no=num).exists():
            data = {
                "status":"0",
                "msg":"Phone number already in use"
            }
            return JsonResponse(data)
        else:
            a = str(random.randrange(10))
            b = str(random.randrange(10))
            c = str(random.randrange(10))
            d = str(random.randrange(10))
            e = str(random.randrange(10))
            f = str(random.randrange(10))
            otp=str(a+b+c+d+e+f)
            print(num+" will recieve "+otp)
            data = {
                "status":"1",
                "msg":otp
            }
            return JsonResponse(data)


def logout(request):
    auth.logout(request)
    return redirect('/')


def forgot(request):
    if request.method == 'GET':
        return render(request,"forgot.html")


def recover_chk(request):
    if request.method == 'POST' and request.is_ajax():
        number = request.POST["number"]
        if User.objects.filter(phone_no=number).exists():
            a = str(random.randrange(10))
            b = str(random.randrange(10))
            c = str(random.randrange(10))
            d = str(random.randrange(10))
            e = str(random.randrange(10))
            f = str(random.randrange(10))
            otp=str(a+b+c+d+e+f)
            print(number+" will recieve "+otp)
            data = {
                "status":"1",
                "msg":otp
            }
            return JsonResponse(data)
        if not User.objects.filter(phone_no=number).exists():
            data = {
                "status":"0",
                "msg":"No Account is associated with this number"
            }
            return JsonResponse(data)


def pass_update(request):
    if request.method == 'POST' and request.is_ajax():
        number = request.POST["number"]
        password = request.POST["password"]
        person = User.objects.get(phone_no=number)
        person.set_password(password)
        person.save()
        data = {
            "status":"1",
            "msg":"login"
        }
        return JsonResponse(data)


def view(request):
    person = request.user
    args = {'per':person}
    return render(request,"profile.html",args)


def see(request,id):
    if request.method == 'GET':
        ad = Post.objects.get(id=id)
        args = {
            "ad":ad
        }
        return render(request,'view.html',args)


def my_item(request,id):
    if request.method == 'GET':
        if request.user.is_authenticated:
            if Post.objects.filter(owner_id=id).exists():
                items = Post.objects.filter(owner_id=id)
                args = {
                    "posts":items
                }
                return render(request,'my_item.html',args)
            else:
                return render(request,'my_item.html')


def delete_item(request,id):
        if request.method == 'GET':
            if request.user.is_authenticated:
                user = request.user
                item = Post.objects.get(id=id)
                item.delete()
                if Post.objects.filter(owner_id=user.id).exists():
                    items = Post.objects.filter(owner_id=user.id)
                    args = {
                        "posts":items
                    }
                    return render(request,'my_item.html',args)
                else:
                    return render(request,'my_item.html')

