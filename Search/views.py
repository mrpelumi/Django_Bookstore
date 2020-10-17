from django.shortcuts import render
from acubook.models import Category,BookInfo,UserProfileInfo
from Carts.models import Cart,CartItem
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
def search(request):
	username = None

	if request.user.is_authenticated:
		username = request.user
		user_profile = UserProfileInfo.objects.get(user=username)
		Cart.objects.get_or_create(currentuser=user_profile)
		carts = Cart.objects.get(currentuser=user_profile)
		cart_items = CartItem.objects.filter(cart=carts)
		total_itemNum =  CartItem.objects.filter(cart=carts).count()

		if request.method == 'GET':
			title = request.GET.get('title').title()
			books = BookInfo.objects.all()
			for book in books:
				if book.Title == title:
					book_category = book.bookcategories.all()[0]
					if str(book_category) == 'Arts and Literature':
						arts = BookInfo.objects.filter(Title = title)
						context = {"arts":arts,'total_cartitem':total_itemNum}
						return render(request,'acubook/bookdescription.html',context)
					elif str(book_category) == 'Science':
						sciences = BookInfo.objects.filter(Title = title)
						context = {"sciences":sciences,'total_cartitem':total_itemNum}
						return render(request,'acubook/bookdescription.html',context)
					elif str(book_category) == 'Christian Books':
						christianbks = BookInfo.objects.filter(Title = t_query)
						context = {"christianbks":christianbks,'total_cartitem':total_itemNum}
						return render(request,'acubook/bookdescription.html',context)
					elif str(book_category) == 'Business':
						business = BookInfo.objects.filter(Title = title)
						context = {"business":business,'total_cartitem':total_itemNum}
						return render(request,'acubook/bookdescription.html',context)
					elif str(book_category) == 'Nigerian and African Authors':
						nigerian = BookInfo.objects.filter(Title = title)
						context = {"nigerian":nigerian,'total_cartitem':total_itemNum}
						return render(request,'acubook/bookdescription.html',context)
					elif str(book_category) == 'Motivational':
						motivational = BookInfo.objects.filter(Title = title)
						context = {"motivational":motivational,'total_cartitem':total_itemNum}
						return render(request,'acubook/bookdescription.html',context)
					elif str(book_category) == 'Teen Books':
						teenbks = BookInfo.objects.filter(Title = title)
						context = {"teenbks":teenbks,'total_cartitem':total_itemNum}
						return render(request,'acubook/bookdescription.html',context)
				#else:
					#return HttpResponse('Book is not available')

	else:
		total_itemNum = 0
		if request.method == 'GET':
			title = request.GET.get('title').title()
			books = BookInfo.objects.all()
			for book in books:
				if book.Title == title:
					book_category = book.bookcategories.all()[0]
					if str(book_category) == 'Arts and Literature':
						arts = BookInfo.objects.filter(Title = title)
						context = {"arts":arts,'total_cartitem':total_itemNum}
						return render(request,'acubook/bookdescription.html',context)
					elif str(book_category) == 'Science':
						sciences = BookInfo.objects.filter(Title = title)
						context = {"sciences":sciences,'total_cartitem':total_itemNum}
						return render(request,'acubook/bookdescription.html',context)
					elif str(book_category) == 'Christian Books':
						christianbks = BookInfo.objects.filter(Title = t_query)
						context = {"christianbks":christianbks,'total_cartitem':total_itemNum}
						return render(request,'acubook/bookdescription.html',context)
					elif str(book_category) == 'Business':
						business = BookInfo.objects.filter(Title = title)
						context = {"business":business,'total_cartitem':total_itemNum}
						return render(request,'acubook/bookdescription.html',context)
					elif str(book_category) == 'Nigerian and African Authors':
						nigerian = BookInfo.objects.filter(Title = title)
						context = {"nigerian":nigerian,'total_cartitem':total_itemNum}
						return render(request,'acubook/bookdescription.html',context)
					elif str(book_category) == 'Motivational':
						motivational = BookInfo.objects.filter(Title = title)
						context = {"motivational":motivational,'total_cartitem':total_itemNum}
						return render(request,'acubook/bookdescription.html',context)
					elif str(book_category) == 'Teen Books':
						teenbks = BookInfo.objects.filter(Title = title)
						context = {"teenbks":teenbks,'total_cartitem':total_itemNum}
						return render(request,'acubook/bookdescription.html',context)
