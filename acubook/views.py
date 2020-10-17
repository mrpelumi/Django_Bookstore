from django.shortcuts import render,redirect
from .forms import UserForm
from django.contrib import messages
from django.http import Http404

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout
from acubook.models import Category,BookInfo,UserProfileInfo
from Carts.models import Cart,CartItem

# Create your views here.
def index(request):
	artsbook = BookInfo.objects.filter(bookcategories__categorys="Arts and Literature")
	sciencebook = BookInfo.objects.filter(bookcategories__categorys="Science")
	christianbook = BookInfo.objects.filter(bookcategories__categorys="Christian Books")
	nigerianbook = BookInfo.objects.filter(bookcategories__categorys="Nigerian and African Authors")
	businessbook = BookInfo.objects.filter(bookcategories__categorys="Business")
	teenbook = BookInfo.objects.filter(bookcategories__categorys="Teen Books")
	motivatebook = BookInfo.objects.filter(bookcategories__categorys="Motivational")

	username = None
	if request.user.is_authenticated:
		username = request.user

		user_profile = UserProfileInfo.objects.get(user=username)
		Cart.objects.get_or_create(currentuser=user_profile)
		carts = Cart.objects.get(currentuser=user_profile)

		cart_items = CartItem.objects.filter(cart=carts)

		total_itemNum =  CartItem.objects.filter(cart=carts).count()
	else:
		total_itemNum = 0

	context = {"artsbook":artsbook,"sciencebook":sciencebook,"christianbook":christianbook,
				"nigerianbook":nigerianbook,"businessbook":businessbook,"teenbook":teenbook,
				"motivatebook":motivatebook,'total_cartitem':total_itemNum}
	return render(request,'acubook/index.html',context)

#FOR cart and order page.Login required will be used.

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('acubook:index'))

def arts(request):
	artsbook = BookInfo.objects.filter(bookcategories__categorys="Arts and Literature")

	username = None
	if request.user.is_authenticated:
		username = request.user

		user_profile = UserProfileInfo.objects.get(user=username)
		Cart.objects.get_or_create(currentuser=user_profile)
		carts = Cart.objects.get(currentuser=user_profile)

		cart_items = CartItem.objects.filter(cart=carts)

		total_itemNum =  CartItem.objects.filter(cart=carts).count()
	else:
		total_itemNum = 0

	context = {"artsbook":artsbook,'total_cartitem':total_itemNum}
	return render(request,'acubook/arts.html',context)

def business(request):
	businessbook = BookInfo.objects.filter(bookcategories__categorys="Business")

	username = None
	if request.user.is_authenticated:
		username = request.user

		user_profile = UserProfileInfo.objects.get(user=username)
		Cart.objects.get_or_create(currentuser=user_profile)
		carts = Cart.objects.get(currentuser=user_profile)
		cart_items = CartItem.objects.filter(cart=carts)

		total_itemNum =  CartItem.objects.filter(cart=carts).count()
	else:
		total_itemNum = 0

	context = {"businessbook":businessbook,'total_cartitem':total_itemNum}
	return render(request,'acubook/business.html',context)

def christian(request):
	christianbook = BookInfo.objects.filter(bookcategories__categorys="Christian Books")

	username = None
	if request.user.is_authenticated:
		username = request.user

		user_profile = UserProfileInfo.objects.get(user=username)
		Cart.objects.get_or_create(currentuser=user_profile)
		carts = Cart.objects.get(currentuser=user_profile)

		cart_items = CartItem.objects.filter(cart=carts)

		total_itemNum =  CartItem.objects.filter(cart=carts).count()
	else:
		total_itemNum = 0

	context = {"christianbook":christianbook,'total_cartitem':total_itemNum}
	return render(request,'acubook/christianbooks.html',context)

def motivational(request):
	motivatebook = BookInfo.objects.filter(bookcategories__categorys="Motivational")

	username = None
	if request.user.is_authenticated:
		username = request.user

		user_profile = UserProfileInfo.objects.get(user=username)
		Cart.objects.get_or_create(currentuser=user_profile)
		carts = Cart.objects.get(currentuser=user_profile)
		cart_items = CartItem.objects.filter(cart=carts)

		total_itemNum =  CartItem.objects.filter(cart=carts).count()
	else:
		total_itemNum = 0

	context = {"motivatebook" : motivatebook,'total_cartitem':total_itemNum}
	return render(request,'acubook/motivational.html',context)

def nigerian(request):
	nigerianbook = BookInfo.objects.filter(bookcategories__categorys="Nigerian and African Authors")

	username = None
	if request.user.is_authenticated:
		username = request.user

		user_profile = UserProfileInfo.objects.get(user=username)
		Cart.objects.get_or_create(currentuser=user_profile)
		carts = Cart.objects.get(currentuser=user_profile)
		cart_items = CartItem.objects.filter(cart=carts)

		total_itemNum =  CartItem.objects.filter(cart=carts).count()
	else:
		total_itemNum = 0

	context = {"nigerianbook":nigerianbook,'total_cartitem':total_itemNum}
	return render(request,'acubook/nigerian.html',context)

def science(request):
	sciencebook = BookInfo.objects.filter(bookcategories__categorys="Science")

	username = None
	if request.user.is_authenticated:
		username = request.user

		user_profile = UserProfileInfo.objects.get(user=username)
		Cart.objects.get_or_create(currentuser=user_profile)
		carts = Cart.objects.get(currentuser=user_profile)
		cart_items = CartItem.objects.filter(cart=carts)

		total_itemNum =  CartItem.objects.filter(cart=carts).count()
	else:
		total_itemNum = 0

	context = {"sciencebook":sciencebook,'total_cartitem':total_itemNum}
	return render(request,'acubook/science.html',context)

def teenbooks(request):
	teenbook = BookInfo.objects.filter(bookcategories__categorys="Teen Books")

	username = None
	if request.user.is_authenticated:
		username = request.user

		user_profile = UserProfileInfo.objects.get(user=username)
		Cart.objects.get_or_create(currentuser=user_profile)
		carts = Cart.objects.get(currentuser=user_profile)

		cart_items = CartItem.objects.filter(cart=carts)

		total_itemNum =  CartItem.objects.filter(cart=carts).count()
	else:
		total_itemNum = 0

	context = {"teenbook":teenbook,'total_cartitem':total_itemNum}
	return render(request,'acubook/teenbooks.html',context)

def about_us(request):
	username = None
	if request.user.is_authenticated:
		username = request.user
		user_profile = UserProfileInfo.objects.get(user=username)
		Cart.objects.get_or_create(currentuser=user_profile)
		carts = Cart.objects.get(currentuser=user_profile)

		cart_items = CartItem.objects.filter(cart=carts)

		total_itemNum =  CartItem.objects.filter(cart=carts).count()
	else:
		total_itemNum = 0
	return render(request,'acubook/aboutus.html',context={'total_cartitem':total_itemNum})

def description(request):
	t_query = request.GET.get("title")
	c_query = request.GET.get("category")
	
	if c_query == 'Arts and Literature':
		arts = BookInfo.objects.filter(Title = t_query)

		username = None
		if request.user.is_authenticated:
			username = request.user
			user_profile = UserProfileInfo.objects.get(user=username)
			Cart.objects.get_or_create(currentuser=user_profile)
			carts = Cart.objects.get(currentuser=user_profile)

			cart_items = CartItem.objects.filter(cart=carts)

			total_itemNum =  CartItem.objects.filter(cart=carts).count()
		else:
			total_itemNum = 0

		context = {"arts":arts,'total_cartitem':total_itemNum}
		return render(request,'acubook/bookdescription.html',context)
		
	elif c_query == 'Science':
		sciences = BookInfo.objects.filter(Title = t_query)

		username = None
		if request.user.is_authenticated:
			username = request.user
			user_profile = UserProfileInfo.objects.get(user=username)
			Cart.objects.get_or_create(currentuser=user_profile)
			carts = Cart.objects.get(currentuser=user_profile)

			cart_items = CartItem.objects.filter(cart=carts)

			total_itemNum =  CartItem.objects.filter(cart=carts).count()
		else:
			total_itemNum = 0
		context = {"sciences":sciences,'total_cartitem':total_itemNum}
		return render(request,'acubook/bookdescription.html',context)

	elif c_query == 'Business':
		business = BookInfo.objects.filter(Title = t_query)

		username = None
		if request.user.is_authenticated:
			username = request.user
			user_profile = UserProfileInfo.objects.get(user=username)
			Cart.objects.get_or_create(currentuser=user_profile)
			carts = Cart.objects.get(currentuser=user_profile)

			cart_items = CartItem.objects.filter(cart=carts)

			total_itemNum =  CartItem.objects.filter(cart=carts).count()
		else:
			total_itemNum = 0
		context = {"business":business,'total_cartitem':total_itemNum}
		return render(request,'acubook/bookdescription.html',context)

	elif c_query == 'Christian Books':
		christianbks = BookInfo.objects.filter(Title = t_query)
		username = None
		if request.user.is_authenticated:
			username = request.user
			user_profile = UserProfileInfo.objects.get(user=username)
			Cart.objects.get_or_create(currentuser=user_profile)
			carts = Cart.objects.get(currentuser=user_profile)

			cart_items = CartItem.objects.filter(cart=carts)

			total_itemNum =  CartItem.objects.filter(cart=carts).count()
		else:
			total_itemNum = 0
		context = {"christianbks":christianbks,'total_cartitem':total_itemNum}
		return render(request,'acubook/bookdescription.html',context)

	elif c_query == 'Motivational':
		motivational = BookInfo.objects.filter(Title = t_query)
		username = None
		if request.user.is_authenticated:
			username = request.user
			user_profile = UserProfileInfo.objects.get(user=username)
			Cart.objects.get_or_create(currentuser=user_profile)
			carts = Cart.objects.get(currentuser=user_profile)
			cart_items = CartItem.objects.filter(cart=carts)

			total_itemNum =  CartItem.objects.filter(cart=carts).count()
		else:
			total_itemNum = 0
		context = {"motivational":motivational,'total_cartitem':total_itemNum}
		return render(request,'acubook/bookdescription.html',context)

	elif c_query == 'Nigerian Books':
		nigerian = BookInfo.objects.filter(Title = t_query)

		username = None
		if request.user.is_authenticated:
			username = request.user
			user_profile = UserProfileInfo.objects.get(user=username)
			Cart.objects.get_or_create(currentuser=user_profile)
			carts = Cart.objects.get(currentuser=user_profile)
			cart_items = CartItem.objects.filter(cart=carts)

			total_itemNum =  CartItem.objects.filter(cart=carts).count()
		else:
			total_itemNum = 0
		context = {"nigerian":nigerian,'total_cartitem':total_itemNum}
		return render(request,'acubook/bookdescription.html',context)

	elif c_query == 'Teen Books':
		teenbks = BookInfo.objects.filter(Title = t_query)
		username = None
		if request.user.is_authenticated:
			username = request.user
			user_profile = UserProfileInfo.objects.get(user=username)
			Cart.objects.get_or_create(currentuser=user_profile)
			carts = Cart.objects.get(currentuser=user_profile)

			cart_items = CartItem.objects.filter(cart=carts)

			total_itemNum =  CartItem.objects.filter(cart=carts).count()
		else:
			total_itemNum = 0
		context = {"teenbks":teenbks,'total_cartitem':total_itemNum}
		return render(request,'acubook/bookdescription.html',context)


#logout user if login and wants to register
	
def register(request):

	registered = False
	username = None
	if request.user.is_authenticated:
		raise Http404("Current User must logout")

	else:

		if request.method == "POST":
			user_form = UserForm(data=request.POST)

			if user_form.is_valid():

				user = user_form.save(commit=False)
				user.set_password(user.password)
				user.save()

				registered = True


				return HttpResponseRedirect(reverse('acubook:user_login'))
			else:
				messages.error(request,"Fill in the form correctly. Passwords must match.")
				return redirect('acubook:register')
		else:
			user_form = UserForm()


		return render(request,'acubook/registeration.html',
						{'user_form':user_form,
							'registered':registered})

def user_login(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username,password=password)

		if user:
			if user.is_active:
				login(request,user)
				return  HttpResponseRedirect(reverse('acubook:index'))
			else:
				messages.info(request,"ACCOUNT NOT ACTIVE")
				return redirect('acubook:user_login')
		else:
			messages.warning(request,"Invalid username or password")
			return redirect('acubook:user_login')
	else:
		return render(request,'acubook/login.html')