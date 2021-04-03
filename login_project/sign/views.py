from django.shortcuts import (
    render,
    redirect
)

from django.http      import HttpResponse

from .models          import Account
from django.views     import View

class SignupView(View):
    def get(self, request):
        return render(request, 'sign/signup.html')

    def post(self, request):
        res_data = {}

        user_name   = request.POST.get('username', None)
        email       = request.POST.get('email', None)
        password    = request.POST.get('password', None)
        re_password = request.POST.get('re_password', None)

        if not (user_name and email and password and re_password):
            res_data['error'] = '모든 값을 입력해야 됩니다.'
        elif Account.objects.filter(user_name = user_name).exists():
            res_data['error'] = '이미 존재하는 이름입니다.'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            user = Account(
                user_name = user_name,
                password = password,
                email = email
            )
            user.save()

        return render(request, 'sign/signup.html', res_data)


class SigninView(View):
    def get(self, request):
        return render(request, 'sign/signin.html')

    def post(self, request):
        res_data = {}
        user_name = request.POST.get('username', None)
        password = request.POST.get('password', None)

        if not (user_name and password):
            res_data['error'] = '모든 값을 입력하세요'

        else:
            user = Account.objects.get(user_name = user_name)
            if user.password == password:
                request.session['user'] = user.id

                return redirect('/')
            else:
                res_data['error'] = '비밀번호가 다릅니다.'

        return render(request, 'sign/signin.html', res_data)

def home(request):
    user_id = request.session.get('user')
    if user_id:
        user = Account.objects.get(pk=user_id)
        return render(request, 'sign/home.html', {'data' : user.user_name})
    return HttpResponse('Home!')
