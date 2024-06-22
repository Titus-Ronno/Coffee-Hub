from django.urls import path
from . import views 


urlpatterns = [
path('home/',views.home, name='home'),
path('', views.landing_page, name='landing_page'),
path('train/', views.cart, name='train'),
path('varieties/', views.card_view, name='varieties'),
path('check-authentication/', views.check_authentication, name='check_authentication'),
#path('protected/', login_required(protected_view), name='protected'),
path('submit-reply/', views.submit_reply, name='submit_reply'),
 path('images/', views.image_view, name='image_view'),
path('reward/', views.rewards, name='Rewards'),
path('event/', views.events, name='Events'),
path('about', views.about, name='about'),
path('schedule-training/', views.schedule_training, name='schedule_training'),
 path('privacy-policy/', views.privacy_policy, name='privacy_policy'),


]