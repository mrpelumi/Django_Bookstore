from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from acubook.views import user_login
from .forms import CartItemForm
from acubook.models import BookInfo,UserProfileInfo
from .models import Cart,CartItem
from django.contrib.auth.models import User
from django.core import validators
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings 
from django.http.response import JsonResponse 
from django.views.decorators.csrf import csrf_exempt
import stripe 

# Create your views here.


def cart(request):
	cart_qty = CartItemForm()
	book_title= request.GET.get("title")
	books = BookInfo.objects.get(Title=book_title)
	book_qty = books.Quantity
	username = None

	if request.user.is_authenticated:
		username = request.user
		if request.method == 'POST':
			quantity = request.POST.get('quantity')

			if int(quantity) > book_qty:
				messages.error(request,'The requested quantity for %s is not available' %(book_title)
				) 
			else:
				user_profile = UserProfileInfo.objects.get(user=username)
				Cart.objects.get_or_create(currentuser=user_profile)
				carts = Cart.objects.get(currentuser=user_profile)
				cart_num = carts.id
				cart_obj = Cart.objects.get(id=cart_num)
				try:
					CartItem.objects.filter(cart=cart_obj,book=books).update(quantity=quantity)
					cart_item = CartItem.objects.filter(cart=cart_obj).get(book=books)

				except CartItem.DoesNotExist:
					CartItem.objects.create(cart=cart_obj,book=books,quantity=quantity)

				cart_items = CartItem.objects.filter(cart=cart_obj)
				total_itemNum =  CartItem.objects.filter(cart=cart_obj).count()
				total_cart = 0
				for item in cart_items:
					total_cart += item.price_subtotal()

				if total_cart == 0:
					context = {'cart_item':cart_items,'total_cartitem':total_itemNum,'total_price':total_cart}
					return render(request,'Carts/cart-empty.html',context)
				else:
					context = {'cart_item':cart_items,'total_cartitem':total_itemNum,'total_price':total_cart}
					return render(request,'Carts/cartpage.html',context)
	else:
		return render(request,'acubook/login.html')


def update_cart(request):
	username = None
	book_title = request.GET.get("title")
	books = BookInfo.objects.get(Title=book_title)
	if request.user.is_authenticated:
		username = request.user

		user_profile = UserProfileInfo.objects.get(user=username)
		Cart.objects.get_or_create(currentuser=user_profile)
		carts = Cart.objects.get(currentuser=user_profile)
		cart_item = CartItem.objects.filter(cart=carts,book=books)
		cart_item.delete()

		cart_items = CartItem.objects.filter(cart=carts)
		total_itemNum =  CartItem.objects.filter(cart=carts).count()
		total_cart = 0
		for item in cart_items:
			total_cart += item.price_subtotal()
		if total_cart == 0:
			context = {'cart_item':cart_items,'total_cartitem':total_itemNum,'total_price':total_cart}
			return render(request,'Carts/cart-empty.html',context)
		else:
			context = {'cart_item':cart_items,'total_cartitem':total_itemNum,'total_price':total_cart}
			return render(request,'Carts/cartpage.html',context)
	else:
		return render(request,'Carts/cartpage.html',{'cart_qty':cart_qty})


def display_cart(request):
	username = None
	if request.user.is_authenticated:
		username = request.user
		user_profile = UserProfileInfo.objects.get(user=username)
		Cart.objects.get_or_create(currentuser=user_profile)
		carts = Cart.objects.get(currentuser=user_profile)

		cart_items = CartItem.objects.filter(cart=carts)

		total_itemNum =  CartItem.objects.filter(cart=carts).count()
		total_cart = 0
		for item in cart_items:
			total_cart += item.price_subtotal()

		if total_cart == 0:
			context = {'cart_item':cart_items,'total_cartitem':total_itemNum,'total_price':total_cart}
			return render(request,'Carts/cart-empty.html',context)
		else:
			context = {'cart_item':cart_items,'total_cartitem':total_itemNum,'total_price':total_cart}
			return render(request,'Carts/cartpage.html',context)
	else:
		return render(request,'acubook/login.html')


def clear_cart(request):
	username = None
	if request.user.is_authenticated:
		username = request.user

		user_profile = UserProfileInfo.objects.get(user=username)
		Cart.objects.get_or_create(currentuser=user_profile)
		carts = Cart.objects.get(currentuser=user_profile)

		cart_items = CartItem.objects.filter(cart=carts)
		cart_items.delete()

		total_itemNum =  0
		total_cart = 0

		context = {'total_cartitem':total_itemNum,'total_price':total_cart}

		return render(request,'Carts/cart-empty.html',context)


def stripe_page(request):
	return render(request,'Carts/stripe_page.html')

@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/cart/stripe-page/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            # Create new Checkout Session for the order
            # Other optional params include:
            # [billing_address_collection] - to display billing address details on the page
            # [customer] - if you have an existing Stripe Customer ID
            # [payment_intent_data] - lets capture the payment later
            # [customer_email] - lets you prefill the email input in the form
            # For full details see https:#stripe.com/docs/api/checkout/sessions/create

            # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'name': 'T-shirt',
                        'quantity': 1,
                        'currency': 'usd',
                        'amount': '2000',
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})