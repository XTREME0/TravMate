from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, PostForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Post
from django.db.models import Q


def index(request):
    query = request.GET.get('q')
    city = request.GET.get('city')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    posts = Post.objects.all().order_by('-created_at')

    if query:
        posts = posts.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )

    if city:
        posts = posts.filter(city__icontains=city)

    if start_date and end_date:
        posts = posts.filter(travel_date__range=[start_date, end_date])
    
    return render(request, 'index.html', {'posts': posts})

def signup(request):
    if request.method == 'POST':
        print("in signuo")
        form = SignUpForm(request.POST)
        if form.is_valid():
            print("form valid")
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.save()
            # Create UserProfile instance
            UserProfile.objects.create(user=user, email=user.email)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    query = request.GET.get('q')
    city = request.GET.get('city')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    posts = Post.objects.all().order_by('-created_at')

    if query:
        posts = posts.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )

    if city:
        posts = posts.filter(city__icontains=city)

    if start_date and end_date:
        posts = posts.filter(travel_date__range=[start_date, end_date])
    
    username = request.user.username
    return render(request, 'home.html', {'posts': posts, 'username': username})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')  # Redirect to home or any other page
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})
