from django.shortcuts import render

# Create your views here.
def login_view(request):
    return render(request, 'login.html')
def register(request):
    return render(request, 'register.html')
def logout_view(request):
    return render(request, 'logout.html')
def my_account(request):
    return render(request, 'my-account.html')