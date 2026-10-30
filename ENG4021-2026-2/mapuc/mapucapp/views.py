from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Movie
from .forms import MovieForm
import requests



def registrar(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        user = User.objects.create_user(username, email, password)
        user.save()
        return redirect("login")
    return render(request, "registro.html")



def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("home")
        else:
            context = {"error_message": "Usuário não existe ou senha incorreta"}
            return render(request, "login.html", context)
    return render(request, "login.html")



def logout_user(request):
    logout(request)
    return redirect("login")

@login_required
def home(request):
    response= requests.get("https://omdbapi.com/?apikey=38b4b85b&s=Batman&type=movie")
    results_json= response.json()
    movies = results_json["Search"]
    context= {
        "movies": movies
    }
    return render(request,"index.html", context)

@login_required
def home2(request):
    movies= Movie.objects.all()
    return render(request, "home.html", {"movies": movies})


@login_required
def movie_create(request):
    form = MovieForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("home")
    return render(request, "movie_form.html", {"form": form, "action": "Novo filme"})


@login_required
def movie_update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    form = MovieForm(request.POST or None, instance=movie)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("home")
    return render(request, "movie_form.html", {"form": form, "action": "Atualizar filme"})


@login_required
def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        movie.delete()
        return redirect("home")
    return render(request, "movie_confirm_delete.html", {"movie": movie})