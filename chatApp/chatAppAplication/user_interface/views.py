"""
    User interface for registration and login
"""

from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User,auth
from django.contrib.sites.shortcuts import get_current_site
from django_short_url.views import get_surl
from django_short_url.models import ShortURL
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from rest_framework.views import APIView
from rest_framework.response import Response
from user_interface.token import token_activation
from user_interface.serializer import UserModelSerilaizer
from chatAppAplication.settings import SECRET_KEY

import jwt

class UserAPI(APIView):

    def get(self,request):
        user = User.objects.all()
        serializer = UserModelSerilaizer(user,many=True)

        return Response(serializer.data)
class RegistrationAPI(APIView):
    
    def get(self,request):

        return render(request,'user/register.html',{})

    def post(self,request):

        firstName = request.POST.get("first_name")
        lastName = request.POST.get("last_name")
        email = request.POST.get("email_id")
        password = request.POST.get("password")
        confirmPassword = request.POST.get("confirm_password")

        if password == confirmPassword:
            user = User.objects.create_user(first_name=firstName,last_name=lastName,username=email,email=email,password=password)
            user.save()

            token = token_activation(user.username, password)

            current_site = get_current_site(request)
            domain = current_site.domain

            url = str(token)

            surl = get_surl(url)

            slug_url = surl.split('/')

            print(slug_url[2])
            mail_subject = "Click below link for activate your acount"

            message = render_to_string('user/email.html',{
                'user' : user.username,
                'domain' : domain,
                'surl' : slug_url[2]
            })

            recipients = email

            email = EmailMessage(mail_subject,message,to=[recipients])
            print(message)
            email.send()

            return HttpResponse("Check your mail and activate your accout")
        
        else:
            return HttpResponse("Password missmatch")

class LoginAPI(APIView):

    def get(self,request):

        return render(request,"user/login.html",{})

    def post(self,request):
        email = request.POST.get('email_id')
        password = request.POST.get('password')
        user = auth.authenticate(username=email,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/chat_page/')

        else:
            return HttpResponse('Inavalid username and password please register')
        

def activate(request,surl):

    try:
        token_object = ShortURL.objects.get(surl=surl)
        token = token_object.lurl
        decode = jwt.decode(token,SECRET_KEY)
        user_name = decode['username']
        user = User.objects.get(username=user_name)

        if user is not None:
            user.is_active = True
            user.save()
            return redirect('/login/')
        else:
            return HttpResponse('Inavalid username and password please register')
    except KeyError:
        return HttpResponse("Key error")

class ForgotPasswordAPI(APIView):
    
    def get(self,request):
        return render(request,'user/forgotpassword.html',{})

    def post(self,request):
        email = request.POST.get('email_id')

        try:
            user = User.objects.filter(email=email)
            useremail = user.values()[0]['email']
            username = user.values()[0]["username"]
            id = user.values()[0]["id"]

            if useremail is not None:
                token = token_activation(username,id)

                url = str(token)
                surl = get_surl(url)
                slug_url = surl.split('/')
                mail_subject = "reset your account password by clicking below link"
                mail_message = render_to_string('user/resetPassword.html', {
                    'user': username,
                    'domain': get_current_site(request).domain,
                    'surl': slug_url[2]
                })
                print(mail_message)
                recipientemail = useremail
                email = EmailMessage(mail_subject, mail_message, to=[recipientemail])
                email.send()

            return HttpResponse("Check your mail")
        except TypeError:

            print("Type error")

class ResetPassword(APIView):

    def get(self,request):
        return render(request,"user/resetpassword_fields.html",{})
    def post(self, request):
        password = request.POST.get("password")
        confirmPassword = request.POST.get("confirm_password")

        if password == confirmPassword:
    
            try:
                user = User.objects.get(username=user_reset)
                user.set_password(password)
                user.save()
                return redirect('/login/')

            except KeyError:
                return HttpResponse("Key Error")

        else:
            return HttpResponse("Password missmatch")

def reset_password(request, surl):
    
    try:
        tokenobject = ShortURL.objects.get(surl=surl)
        token = tokenobject.lurl
        decode = jwt.decode(token, SECRET_KEY)
        username = decode['username']
        user = User.objects.get(username=username)

        if user is not None:
            return redirect('/resetpassword/'+str(user))
        else:
            return redirect('/forgotpassword/')
    except KeyError:
        return HttpResponse("Key Error")

def chat_page(request):

    return render(request,'user/chat_page.html',{})

