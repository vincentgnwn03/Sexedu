# sexeduapp/urls.py
from django.conf import settings  # type: ignore
from django.conf.urls.static import static  # type: ignore
from django.urls import path  # type: ignore

from . import views

app_name = 'sexeduapp'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('course/', views.course, name='course'),
    path('class_content/', views.class_content, name='class_content'),
    path('login/', views.login, name='loginpage'),
    path('register/', views.register, name='register'),
    path('report/', views.report, name='report'),
    path('about/', views.about, name='about'),
    path("user_login/", views.user_login, name="user_login"),
    path("dashboardcontent/", views.dashboardcontent, name="dashboardcontent"),
    path("dashboardcourse/", views.dashboardcourse, name="dashboardcourse"),
    path("dashboardstudent/", views.dashboardstudent, name="dashboardstudent"),
    path('pesanberhasil/', views.pesanberhasil, name='pesanberhasil'), 
    path('laporan/', views.Laporan, name='Laporan'),
    path('report_view/', views.report_view, name='report_view'),
    path('pesanberhasil/', views.pesanberhasil_view, name='pesanberhasil'),
    path('profile/', views.profile, name='profile'),
       
     
    # URL pattern lainnya
] 




