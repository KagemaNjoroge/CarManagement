import json
from django.http import JsonResponse
from django.shortcuts import redirect, render
from rest_framework.viewsets import ModelViewSet
from .serializers import CustomUserSerializer, CustomUser
from django.contrib.auth import authenticate, login

# methods required decorator
from django.views.decorators.http import require_http_methods


class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


# logout, login
from django.contrib.auth import logout


@require_http_methods(["GET", "POST"])
def login_page(request):
    if request.user.is_authenticated:
        return redirect("/home/")
    else:

        if request.method == "GET":
            return render(request, "authentication/login.html")
        else:

            data = json.loads(request.body)
            username = data.get("username")
            password = data.get("password")

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)

                return JsonResponse({"message": "success"})
            else:
                return JsonResponse({"message": "Invalid email or password!"})


@require_http_methods(["GET", "POST"])
def register_page(request):
    # logout user if already logged in
    if request.user.is_authenticated:
        logout(request)

    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        user = CustomUser.objects.create_user(
            username=username, email=email, password=password
        )

        return JsonResponse({"message": "success"})
    else:
        return render(request, "authentication/register.html")
