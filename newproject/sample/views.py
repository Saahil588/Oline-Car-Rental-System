from django.shortcuts import render,redirect,HttpResponse
from .models import CarBooking, Contact, OfferBooking,User,Offers,Addcar,Images,Car,Booking
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')

def terms(request):
    return render(request,'terms.html')


#register
def register(request):
    if request.method == 'GET':
        return render(request,'register.html',)
    else:
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        username = request.POST.get('uname')
        password = request.POST.get('password')
        age = request.POST.get('age')
        email = request.POST.get('email')
        ph = request.POST.get('ph')
        address = request.POST.get('address')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')
        User.objects.create_user(first_name=first_name,last_name=last_name,username=username,
        password=password,age=age,email=email,ph=ph,address=address,city=city,pincode=pincode,usertype="normaluser")
        return redirect(login_user) 

#login user
def login_user(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        check = authenticate(request,username=username,password=password)
        if check is not None:
            if check .usertype == "normaluser":
                login(request,check)
                return redirect(user_fn)
            elif check .usertype =="True":
                login(request,check)
                return redirect(admin_fn)
            else:
                return redirect(home)
        else:
            return redirect(register)
    else:
        return render(request,'login.html')

#edit profile
@login_required(login_url="/login/")
def edit_profile(request):
    if request.method == 'POST':
        users = User.objects.get(pk=request.user.id)
        users.first_name = request.POST.get('fname')
        users.last_name = request.POST.get('lname')
        users.username = request.POST.get('uname')
        users.age = request.POST.get('age')
        users.email = request.POST.get('email')
        users.ph = request.POST.get('ph')
        users.address = request.POST.get('address')
        users.city = request.POST.get('city')
        users.pincode = request.POST.get('pincode')
        users.save()
        return redirect(user_fn)
    else:
        users = User.objects.get(pk=request.user.id)
        return render(request,'edit_profile.html',{'data':users})

#admin view by user 
@login_required(login_url="/login/")   
def view_user(request):
    users= User.objects.all().filter(usertype='normaluser')
    return render(request,'view_user.html',{'data':users})    

#delete user
def delete_user(request,id):
    users = User.objects.get(pk=id)
    users.delete()
    return redirect(view_user)



 #change password
@login_required(login_url="/login/")
def change_password(request):
    context={}
    ch = User.objects.filter(pk=request.user.id)
    if len(ch)>0:
        data = User.objects.get(pk=request.user.id)
        context["data"] = data
    if request.method=="POST":
        current = request.POST["cpwd"]
        new_pas = request.POST["npwd"]
        
        user = User.objects.get(id=request.user.id)
        un = user.username
        check = user.check_password(current)
        if check==True:
            user.set_password(new_pas)
            user.save()
            context["msz"] = "Password Changed Successfully!!!"
            context["col"] = "alert-success"
            user = User.objects.get(username=un)
            login(request,user)
        else:
            context["msz"] = "Incorrect Current Password"
            context["col"] = "alert-danger"

    return render(request,"changeps.html",context)



#feedback 
def contact(request):
    if request.method == 'POST':
        cnt = Contact()
        cnt.name = request.POST.get('name')
        cnt.email = request.POST.get('email')
        cnt.ph = request.POST.get('ph')
        cnt.message = request.POST.get('message')
        cnt.save()
        return redirect(contact)
    else:
         return render(request,'contact.html')


# view feedback
@staff_member_required(login_url="/login/")
def view_contact(request):
    cnt = Contact.objects.all()
    return render(request,'view_contact.html',{'data':cnt})


#delete feedback
@staff_member_required(login_url="/login/")
def del_contact(request,id):
    if request.method =='GET':
        cnt = Contact.objects.get(pk=id)
        cnt.delete()
        return redirect(view_contact)


#add offer by admin
@staff_member_required(login_url="/login/")
def adminoffer(request):
    if request.method == 'POST':
        offer = Offers()
        offer.title = request.POST.get('title')
        offer.description = request.POST.get('description') 
        offer.actual_price = request.POST.get('actual_price')
        offer.offer = request.POST.get('offer')
        image = request.FILES['images']
        offer.image = image
        offer.save()
        return redirect(admin_fn)
    else:
         return render(request,'adminoffer.html')

#view by user offer
def offers(request):
    offer = Offers.objects.all()
    return render(request,'offers.html',{'data':offer})

# admin view offer
@login_required(login_url="/login/")   
def adview_offer(request):
    offer = Offers.objects.all()
    return render(request,'view_offer.html',{'data':offer})    


#edit offer
@staff_member_required(login_url="/login/")
def edit_adminoffer(request,id):
    if request.method == 'POST':
        offer = Offers.objects.get(pk=id)
        offer.title = request.POST.get('title')
        offer.description = request.POST.get('description') 
        offer.actual_price = request.POST.get('actual_price')
        offer.offer = request.POST.get('offer')
        image = request.FILES.get('image')
        if image:
            offer.image = image
        offer.save()
        return redirect(adview_offer)
    else:
        offer = Offers.objects.get(pk=id)
        return render(request,'edit_offer.html',{'data':offer})

#delete offer
def del_adminoffer(request,id):
    offer = Offers.objects.get(pk=id)
    offer.delete()
    return redirect(adview_offer)

#offer images
@login_required(login_url="/login/")
def offer_images(request,id):
    ofr = Offers.objects.get(pk=id)
    return render(request,'offer_images.html',{'data':ofr})

#offer booking
def offer_booking(request,id):
    if request.method == 'POST': 
        user = User.objects.get(pk=request.user.id)
        offer = Offers.objects.get(pk=id)
        book = OfferBooking()
        book.offers_id = offer.id
        book.user_id = user.id
        user.cname = request.POST.get('username')
        user.ph = request.POST.get('ph')
        user.email = request.POST.get('email')
        book.title = request.POST.get('title')
        book.description = request.POST.get('description') 
        book.actual_price = request.POST.get('actual_price')
        book.offer = request.POST.get('offer')
        book.pickup_date = request.POST.get('pickup_date')
        book.dropoff_date = request.POST.get('dropoff_date')
        book.pickup_address = request.POST.get('pickup_address')
        book.dropoff_address = request.POST.get('dropoff_address')
        book.save()
        return redirect(user_fn)
    else:
        user = User.objects.get(pk=request.user.id)
        offer = Offers.objects.get(pk=id)
        return render(request,'offer_booking.html',{'data':user,'offers':offer})   

#admin view by offerbooking 
@login_required(login_url="/login/")   
def view_offerbooking(request):
    book = OfferBooking.objects.all()
    offer = Offers()
    return render(request,'view_offerbooking.html',{'data':book,'offers':offer})    

#delete view offerbooking 
def delete_offerbooking(request,id):
    book = OfferBooking.objects.get(pk=id)
    book.delete()
    return redirect(view_offerbooking)

#user view by offerbooking 
@login_required(login_url="/login/")   
def user_viewoffer(request):
    book = OfferBooking.objects.all()
    offer = Offers()
    return render(request,'user_viewoffer.html',{'data':book,'offers':offer})    

#delete view offerbooking user
def delete_useroffer(request,id):
    book = OfferBooking.objects.get(pk=id)
    book.delete()
    return redirect(user_viewoffer)


#add car by admin (rentcar)
@staff_member_required(login_url="/login/")
def addcar(request):
        if request.method == 'POST':
            car = Addcar()
            car.car_name = request.POST.get('car_name')
            car.color = request.POST.get('color')
            car.city = request.POST.get('city')
            car.pincode = request.POST.get('pincode')
            car.description = request.POST.get('description')
            car.capacity = request.POST.get('capacity')
            car.rate = request.POST.get('rate')
            car.save()
            return redirect(admin_fn)
        else:
            return render(request,'addcar.html')


#display in userbase (rentcar)
@login_required(login_url="/login/")
def user_addcar(request):
    car = Addcar.objects.all()
    return render(request,'user_addcar.html',{'data':car})    


#edit addcar(rentcar)
@staff_member_required(login_url="/login/")
def edit_adminaddcar(request,id):
    if request.method == 'POST':
        car = Addcar.objects.get(pk=id)
        car.car_name = request.POST.get('car_name')
        car.color = request.POST.get('color')
        car.city = request.POST.get('city')
        car.pincode = request.POST.get('pincode')
        car.description = request.POST.get('description')
        car.capacity = request.POST.get('capacity')
        car.rate = request.POST.get('rate')
        car.save()
        return redirect(adview_addcar)
    else:
        car = Addcar.objects.get(pk=id)
        return render(request,'edit_addcar.html',{'data':car})

#delete addcar(rentcar)
def del_adminaddcar(request,id):
    car = Addcar.objects.get(pk=id)
    car.delete()
    return redirect(adview_addcar)


#admin view by addcar (rentcar)
@login_required(login_url="/login/")   
def adview_addcar(request):
    car = Addcar.objects.all()
    return render(request,'view_addcar.html',{'data':car})    

#rentcar booking 
def booking(request,id):
    if request.method == 'POST': 
        user = User.objects.get(pk=request.user.id)
        book = Booking()
        book.user_id = user.id
        book.cname = request.POST.get('username')
        book.ph = request.POST.get('ph')
        book.email = request.POST.get('email')
        book.capacity = request.POST.get('capacity')
        book.pickup_date = request.POST.get('pickup_date')
        book.dropoff_date = request.POST.get('dropoff_date')
        book.pickup_address = request.POST.get('pickup_address')
        book.dropoff_address = request.POST.get('dropoff_address')
        book.total_days = request.POST.get('days')
        book.rate_perday = request.POST.get('rate_perday')
        book.rate = request.POST.get('rate')
        book.save()
        return redirect(user_fn)
    else:
        user = User.objects.get(pk=request.user.id)
        addcar = Addcar.objects.get(pk=id)
        return render(request,'booking.html',{'data':user,'car':addcar})

#admin view by booking (rentcar)
@login_required(login_url="/login/")   
def view_booking(request):
    book = Booking.objects.all()
    return render(request,'view_booking.html',{'data':book})    

#delete viewbooking(rentcar)
def delete_booking(request,id):
    book = Booking.objects.get(pk=id)
    book.delete()
    return redirect(view_booking)


#add car by admin (cars)
@staff_member_required(login_url="/login/")
def admincar(request):
    if request.method == 'POST':
        cars = Car()
        cars.car_name = request.POST.get('car_name')
        cars.car_type = request.POST.get('car_type') 
        cars.company_name = request.POST.get('company_name')
        cars.rate = request.POST.get('rate')
        image = request.FILES['image']
        cars.image = image
        cars.save()
        return redirect(admin_fn)
    else:
         return render(request,'admincar.html')


# display in userbase (cars)
@login_required(login_url="/login/")
def car(request):
    cars = Car.objects.all()
    return render(request,'car.html',{'data':cars})  

# admin view cars (cars)
@login_required(login_url="/login/")   
def adview_car(request):
    cars = Car.objects.all()
    return render(request,'view_car.html',{'data':cars})    


#edit cars (cars)
@staff_member_required(login_url="/login/")
def edit_admincar(request,id):
    if request.method == 'POST':
        cars = Car.objects.get(pk=id)
        cars.car_name = request.POST.get('car_name')
        cars.car_type = request.POST.get('car_type') 
        cars.company_name = request.POST.get('company_name')
        cars.rate = request.POST.get('rate')
        image = request.FILES.get('image')
        if image:
            cars.image = image
        cars.save()
        return redirect(adview_car)
    else:
        cars = Car.objects.get(pk=id)
        return render(request,'edit_car.html',{'data':cars})

        
#delete cars (cars)
def del_admincar(request,id):
    cars = Car.objects.get(pk=id)
    cars.delete()
    return redirect(adview_car)

#car booking
def car_booking(request,id):
    if request.method == 'POST':
        user = User.objects.get(pk=request.user.id)
        book = CarBooking()
        book.user_id = user.id
        book.cname = request.POST.get('username')
        book.ph = request.POST.get('ph')
        book.email = request.POST.get('email')
        book.pickup_date = request.POST.get('pickup_date')
        book.dropoff_date = request.POST.get('dropoff_date')
        book.pickup_address = request.POST.get('pickup_address')
        book.dropoff_address = request.POST.get('dropoff_address')
        book.total_days = request.POST.get('total_days')
        book.rate_perday = request.POST.get('rate_perday')
        book.rate = request.POST.get('rate')
        book.save()
        return redirect(user_fn)
    else:
        user = User.objects.get(pk=request.user.id)
        car = Car.objects.get(pk=id)
        return render(request,'car_booking.html',{'data':user,'car':car})   

#admin view by carbooking (car)
@login_required(login_url="/login/")   
def view_carbooking(request):
    book = CarBooking.objects.all()
    return render(request,'view_carbooking.html',{'data':book})    

#delete view carbooking (car)
def delete_carbooking(request,id):
    book = CarBooking.objects.get(pk=id)
    book.delete()
    return redirect(view_carbooking)

#user view by carbooking (car)
@login_required(login_url="/login/")   
def user_viewcarbook(request):
    book = CarBooking.objects.all()
    return render(request,'user_viewcarbook.html',{'data':book})    

#delete view carbooking user (car)
def delete_carbook(request,id):
    book = CarBooking.objects.get(pk=id)
    book.delete()
    return redirect(user_viewcarbook)

#add image by admin (Gallery)
@staff_member_required(login_url="/login/")
def adminimage(request):
    if request.method == 'POST':
        img = Images()
        img.title = request.POST.get('title')
        img.stock = request.POST.get('stock')
        image = request.FILES['images']
        img.image = image
        img.save()
        return redirect(admin_fn)
    else:
        return render(request,'adminimage.html')

# view in userbase (Gallery)
@login_required(login_url="/login/")
def user_image(request):
    img = Images.objects.all()
    return render(request,'user_image.html',{'data':img})


# admin view (Gallery)
@login_required(login_url="/login/")   
def adview_image(request):
    img = Images.objects.all()
    return render(request,'view_image.html',{'data':img})    


#edit image (Gallery)
@staff_member_required(login_url="/login/")
def edit_adminimage(request,id):
    if request.method == 'POST':
        img = Images.objects.get(pk=id)
        img.title = request.POST.get('title')
        img.stock = request.POST.get('stock') 
        image = request.FILES.get('image')
        if image:
            img.image = image
        img.save()
        return redirect(adview_image)
    else:
        img = Images.objects.get(pk=id)
        return render(request,'edit_image.html',{'data':img})

#delete image (Gallery)
def del_adminimage(request,id):
    img = Images.objects.get(pk=id)
    img.delete()
    return redirect(adview_image)


#admin view by booking (rentcar)
@login_required(login_url="/login/")   
def user_view(request):
    book = Booking.objects.all()
    return render(request,'user_view.html',{'data':book})    

#delete viewbooking(rentcar)
def delete_userview(request,id):
    book = Booking.objects.get(pk=id)
    book.delete()
    return redirect(user_view)

def adminbase(request):
    return render(request,'adminbase.html')

def userbase(request):
    return render(request,'userbase.html')

def admin_fn(request):
    return render(request,'admin.html')

def user_fn(request):
    return render(request,'user.html')


@staff_member_required(login_url="/login/")
def logout_admin(request):
    logout(request)
    return redirect(login_user)

@login_required(login_url="/login/")
def logout_user(request):
    logout(request)
    return redirect(login_user)
