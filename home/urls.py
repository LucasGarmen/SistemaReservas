from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('charts/', views.charts, name='charts'),
    path('tables/', views.tables, name='tables'),
    path('buttons/', views.buttons, name='buttons'),
    path('cards/', views.cards, name='cards'),
    path('register/', views.register, name='register'),
    path('forgot_password/' ,views.forgot_password, name='forgot_password'),
    path('blank/' ,views.blank, name='blank'),
    path('utilities-color/', views.utilities_color, name='utilities-color'),
    path('404/', views.page_404, name='404'),
    path('utilities_other', views.utilities_other, name='utilities_other'),
    path('utilities_border', views.utilities_border, name='utilities_border'),
    path('utilities_animation', views.utilities_animation, name='utilities_animation'),
    path('utilities_color', views.utilities_color, name='utilities_color'),

    
]