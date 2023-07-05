from django.shortcuts import render
from django.contrib import auth
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User

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
        
class MyInfo(APIView):
    def get(self, request):
        user = request.user

        if user is not None:
            return Response({"message": user.id})
        else:
            return Response({"message": "로그아웃 상태입니다."})