from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('frequently-asked-questions', views.faq, name='faq'),
    path('about-us/', views.about_us, name='about_us'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-condition/', views.terms_condition, name='terms_condition'),
]
