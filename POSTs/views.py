from django.shortcuts import render,redirect
from .models import Post
# Create your views here.
def poster(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request,"ad_upload.html")
        else:
            return redirect('login')


def post(request):
    if request.method == 'POST':
        title  = request.POST["Title"]
        price = request.POST["price"]
        owner = request.user
        categorie = request.POST["categoire"]
        time = request.POST["time"]
        location = request.POST["location"]
        describtion = request.POST["item_des"]
        img1 = request.FILES["img1"]
        img2 = request.FILES["img2"]
        img3 = request.FILES["img3"]
        img4 = request.FILES["img4"]
        img5 = request.FILES["img5"]
        img6 = request.FILES["img6"]
        ad = Post(
            Title = title,
            owner = owner,
            price = price,
            describtion = describtion,
            img1 = img1,
            img2 = img2,
            img3 = img3,
            img4 = img4,
            img5 = img5,
            img6 = img6,
            old = time,
            region = location
        )
        ad.save()
        return redirect('/')