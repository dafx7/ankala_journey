from django.urls import path
from . import views

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('cv/<int:id>', views.tour_guide_cv, name='cv'),
    path('cv/<int:id>/reviews', views.tour_guide_reviews, name='reviews'),
    path('frequently-asked-questions', views.faq, name='faq'),
    path('about-us/', views.about_us, name='about_us'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-condition/', views.terms_condition, name='terms_condition'),
    path('payment/', views.payment, name='payment'),
]
