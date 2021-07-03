from django.shortcuts import render
from django.http import HttpResponse
from bankapp.models import Banking
from django.contrib.auth.models import auth,User
from django.contrib.auth import logout
# Create your views here.
def homepage(request):
	#return HttpResponse('<h1>WELCOME TO MY HOMEpage.</h1>')
	return render(request,'bankproject/homepage.html')

def register(request):
	return render(request, 'bankproject/new_registration.html')

def new_registration(request):
	if request.method == "POST" :
		name1=request.POST["name"]
		id1=request.POST["id"]
		email1=request.POST["email"]
		phone_no1=request.POST["phone_no"]
		balance1=request.POST["balance"]
		qset1=Banking.objects.filter(c_emailid=email1,c_phone_no=phone_no1)
		for items in qset1:
			print(items.c_name)
		print(qset1)
		if len(qset1)==0:
			user = Banking(c_name=name1, c_id=id1, c_emailid=email1, c_phone_no=phone_no1, c_balance=balance1)
			user.save()
			if user is not None:
				print("User created")
				return render(request,'bankproject/homepage.html')
		else:
			print('user not created')
			return HttpResponse('<h1>User is not created,emailid,or password already exist</h1>')
	else:
		return HttpResponse('<h1>request is of type get </h1>')
def new_user(request):
	return render(request,"bankproject/new_user_form.html")

def create_user(request):
	if request.method == "POST":
		username1=request.POST["u_name"]
		password1=request.POST["u_password"]
		user=auth.authenticate(username=username1,password=password1)
		if user is None:
			obj=User.objects.create_user(username=username1,password=password1)
			obj.save()
			return render(request,'bankproject/user_created.html',{"USERNAME":username1,"PASSWORD":password1})
		else:
			return HttpResponse(" username or password already exist ")
	else:
		return HttpResponse(" request is of type GET ")

def login_form(request):
	return render(request,'bankproject/login_form.html')
def login(request):
	if request.method == "POST":
		username1 = request.POST["name"]
		password1 = request.POST["password"]
		obj=auth.authenticate(username=username1,password=password1)
		if obj is not None:
			return render(request, 'bankproject/homepage.html', {"user":obj})
		else:
			return render(request, 'bankproject/homepage.html')
	else:
		return HttpResponse("request method is of type GET")



def show_details(request):
	obj=Banking.objects.all()
	return render(request, 'bankproject/show_details.html', {"qset": obj})

def logout1(request):
	logout(request)
	return render(request, 'bankproject/homepage.html', {"name": "logged out"})





