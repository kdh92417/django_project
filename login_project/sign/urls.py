from django.urls    import path
from .              import views

app_name = 'sign'
urlpatterns = [
    path('sign-up/', views.SignupView.as_view()),
    path('sign-in/', views.SigninView.as_view()),

]
