from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from.models import Room,Booking

# Create your views here.

def home(request):
    return render(request,'home.html')

def register_user(request):
    if request.method=="POST":
        User.objects.create_user(
            username=request.POST['username'],password=request.POST['password']
        )
        return redirect('login')
    return render(request,'register.html')

def login_user(request):
    if request.method=="POST":
        user=authenticate(
            username=request.POST['username'],password=request.POST['password']
        )
        if user is not None:
            login(request,user)
            return redirect('rooms')
        else:
            return render(request,'login.html',{'error':'invalid username or password'})
    return render(request,'login.html')
    
def logout_user(request):
    logout(request)
    return redirect('home')
    
def rooms(request):
        rooms_list= Room.objects.filter(available=True)
        return render(request,'rooms.html',{'rooms':rooms_list})
    
def book_room(request,room_id):
    if request.method=="POST":
        room = Room.objects.get(id=room_id)
        booking=Booking.objects.create(
            user=request.user,
            room=room,
            check_in=request.POST['check_in'],
check_out=request.POST['check_out']
        )
        room.available=False
        room.save()

        return render(request,'booking_result.html',{'booking':booking})
        
