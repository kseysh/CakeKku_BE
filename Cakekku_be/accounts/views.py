from django.shortcuts import render
from django.contrib import auth
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from drf_yasg.utils import swagger_auto_schema

class Signup(APIView):
    def post(self, request):
        user = User.objects.create_user(
            userID = request.data["userID"],
            password = request.data["password"]
        )
        return Response({"message": "Success Signup!"}, status = 200)
    
class Login(APIView):
    def post(self, request):
        userID = request.data["userID"]
        password = request.data["password"]

        user = auth.authenticate(userID = userID, password = password)

        if user is not None:
            auth.login(request, user)
            return Response({"id": user.id}, status = 200)
        else:
            return Response({"message": "유저 정보가 없습니다"}, status = 403)
        
class Logout(APIView):
    def post(self, request):
        auth.logout(request)
        return Response({"message": "로그아웃 되었습니다."}, status=200)
    
class MyInfo(APIView):
    def get(self, request):
        user = request.user

        if user is not None:
            return Response({"message": user.id})
        else:
            return Response({"message": "로그아웃 상태입니다."})


from django.contrib import auth

class LoginTempUser(APIView):
    @swagger_auto_schema(tags=['임시 유저로 로그인'], responses={200: 'Success'})
    def get(self, request):
        username = "user"
        password = "1234"        
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return Response({"id": user.id}, status=200)
        else:
            return Response({"error": "Invalid credentials"}, status=400)

    
