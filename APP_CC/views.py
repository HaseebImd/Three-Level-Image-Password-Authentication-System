from django.shortcuts import render
import requests
from django.views import View
from django.http import HttpResponse
import re
from .models import Authentication


class Home(View):
    def post(self, request, *args, **kwargs):
        return render(request, 'home.html')
class Index(View):
    # greeting = "Good Day"

    def get(self, request):
        return render(request, 'index.html')

    # def post(self, request, *args, **kwargs):
    #     emailAddress = request.POST.get('emailAddress')
    #     password = request.POST.get('password')
    #     print("Email", emailAddress)
    #     return render(request, 'loginByPic.html')
    # def get(self, request):
    #     return render(request, 'index.html')

    # def post(self, request, *args, **kwargs):
    #     emailAddress = request.POST.get('emailAddress')
    #     password = request.POST.get('password')
    #     print("Email", emailAddress)
    #     return render(request, 'loginByPic.html')

class LoginByEmailPassword(View):
    def post(self, request, *args, **kwargs):
        emailAddress = request.POST.get('emailAddress')
        password = request.POST.get('password')
        print("Email", emailAddress,"password",password)
        try:
            user = Authentication.objects.get(
                email=emailAddress, password=password)
            if user is not None:
                return render(request, 'loginByPic.html', {})
            else:
                print("Someone tried to login and failed.")
                return render(request, 'login.html', {'error':'Invalid Credentials'})
        except Exception as identifier:
            print("Exceptoin called")
            print(identifier)
            return render(request, 'login.html', {'error': 'Invalid Credentials'})


class LoginEP(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request, *args, **kwargs):
        return render(request, 'login.html')


class SignUpEP(View):
    
    def post(self, request, *args, **kwargs):
        return render(request, 'signup.html')


class LoginbyPic(View):

    def post(self, request, *args, **kwargs):
        loginByPICData = request.POST.get('userSelection')
        
        try:
            user = Authentication.objects.get(
                withPic=loginByPICData)
            if user is not None:
                return render(request, 'selectPicPatteren.html', {})
            else:
                print("Someone tried to login and failed.")
                return render(request, 'loginByPic.html')
        except Exception as identifier:
            print("Exceptoin called")
            print(identifier)
            return render(request, 'loginByPic.html', {'error': 'Invalid Credentials'})


class SignUpbyPic(View):

    def post(self, request, *args, **kwargs):

        userSelection = request.POST.get('userSelection')
        
        if Authentication.objects.update(withPic=userSelection):
            return render(request, 'index.html', {'error': 'Created Successfulyl'})
        else:
            return render(request, 'signUpByPic.html', {'error': 'Unable to Create'})


        # loginByPICData = request.POST.get('userSelection')
        # try:
        #     user = Authentication.objects.get(
        #         withPic=loginByPICData)
        #     if user is not None:
        #         return render(request, 'selectPicPatteren.html', {})
        #     else:
        #         print("Someone tried to login and failed.")
        #         return render(request, 'loginByPic.html')
        # except Exception as identifier:
        #     print("Exceptoin called")
        #     print(identifier)
        #     return render(request, 'loginByPic.html', {'error': 'Invalid Credentials'})
        

class SignUpByEmailPassword(View):

    def post(self, request, *args, **kwargs):
        emailAddress = request.POST.get('emailAddress')
        password = request.POST.get('password')
        print("Email", emailAddress, "password", password)
        try:
            
            user = Authentication()
            user.email = emailAddress
            user.password = password
            user.withPic=''
            print(user)
            context = {'error': 'Created Successfully'}
            if user.save():
                return render(request, 'signUpByPic.html', {'context': context})
            else:
                
                return render(request, 'signUpByPic.html', {'context': context})
            
        except Exception as identifier:
            print("Exceptoin called")
            print(identifier)
            return render(request, 'index.html')
