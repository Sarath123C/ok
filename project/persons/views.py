from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .forms import PersonCreationForm
from .models import Person, Course


def home(request):
    return render(request, 'index.html')


def register(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        # login(request, user)
        return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def loginn(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('person_add')
        else:
            return HttpResponse("not user")
    return render(request, 'login.html')


def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        pDict = request.POST.copy()
        form = PersonCreationForm(pDict)
        if form.is_valid():
            form.save()
            form = PersonCreationForm()
    return render(request, 'home.html', {'form': form})





def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('login', pk=pk)

    return render(request, 'home.html', {'form': form})


# AJAX
def load_courses(request):
    department_id = request.GET.get('department_id')
    course = Course.objects.filter(department_id=department_id).all()
    return render(request, 'city_dropdown_list_options.html', {'course': course})


def logout(request):
    auth.logout(request)
    return redirect('/')
