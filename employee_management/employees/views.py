from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages



@login_required
def employee_list(request):
    # Replace this with logic to fetch employee data from your models
    employees = []  # Placeholder for actual employee data
    return render(request, 'employees/employee_list.html', {'employees': employees})



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            messages.success(request, 'Registration successful!')
            return redirect('employee_list')  # Redirect to the employee list page
    else:
        form = UserCreationForm()
    return render(request, 'employees/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('employee_list')  # Redirect to the employee list page
        else:
            messages.error(request, 'Invalid username or password.')
            # Render the login page with the error message
    return render(request, 'employees/login.html')



@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'You have logged out successfully!')
    return redirect('login')  # Redirect to the login page
