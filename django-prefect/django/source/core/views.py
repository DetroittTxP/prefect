from django.shortcuts import render
from rest_framework import viewsets
from create_user import create_users_flow
from rest_framework.response import Response
# Create your views here.


class UserViewSet(viewsets.ViewSet):
    def post(self, request):
        create_users_flow(request.data)
        return Response({"status": "Users created successfully"})
