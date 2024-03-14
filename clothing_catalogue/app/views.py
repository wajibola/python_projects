from django.shortcuts import redirect, render
# from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from rest_framework import status

# Create your views here.
def home(request):
    return render(request, "home.html")

def login(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        """ user = authenticate(
            username=username,
            password=password
        ) """

        if username and password:
            # login(request, user)
            # return JsonResponse({"message": "Login Successful"}, status=status.HTTP_200_OK)
            return redirect("/catalogue")

        else:
            return JsonResponse({"message": "Invalid username or password"}, status=status.HTTP_400_BAD_REQUEST)
    
    return render(request, "login.html")
    

# def logout(request):
#     # logout(request)
#     return JsonResponse({'message': 'Logout successful'}, status=status.HTTP_200_OK)

def catalogue(request):
    return render(request, "catalogue.html")