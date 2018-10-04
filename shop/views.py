from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Category, Product
from django.contrib.auth.models import Group, User
# from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

def index(request):
  text_var = 'This is my first django web app.'
  return HttpResponse(text_var)

def all_products(request):
  products = Product.objects.filter(available=True)
  return render(request, 'shop/index.html', {'products':products})

def product_detail(request, product_slug):
  try: 
    product = Product.objects.get(slug=product_slug)
  except Exception as e:
    raise e
  return render(request, 'shop/product.html', {'product':product})

def commission(request):
  try: 
    products = Product.objects.filter(commission=True)
  except Exception as e:
    raise e
  return render(request, 'shop/commission.html', {'products':products})

def signupView(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      signup_user = User.objects.get(username=username)
      customer_group = Group.objects.get(name='Customer')
      customer_group.user_set.add(signup_user)
      # messages.success(request, 'Account created successfully')
      # return redirect('signup')
  else: 
    form = SignUpForm()
  return render(request, 'accounts/signup.html', {'form':form})

# def signupView(request):
# 	if request.method == 'POST':
# 		form = SignUpForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			username = form.cleaned_data.get('username')
# 			signup_user = User.objects.get(username=username)
# 			customer_group = Group.objects.get(name='Customer')
# 			customer_group.user_set.add(signup_user)
# 	else:
# 		form = SignUpForm()
# 	return render(request, 'accounts/signup.html', {'form':form})

def signinView(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('shop:all_products')
			else:
				return redirect('signup')
	else:
		form = AuthenticationForm()
	return render(request, 'accounts/signin.html', {'form':form})

def signoutView(request):
	logout(request)
	return redirect('signin')
