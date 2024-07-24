from django.conf import settings  # type: ignore
from django.conf.urls.static import static  # type: ignore
from django.contrib import admin  # type: ignore
from django.urls import include, path  # type: ignore
from sexeduapp import views
from sexeduapp.views import editcourse

urlpatterns = [
    # Path untuk halaman utama atau index
    path('', views.index, name='index'),

    # Path untuk admin Django
    path('admin/', admin.site.urls),

    # Path untuk aplikasi sexeduapp
    path('sexeduapp/', include('sexeduapp.urls')),
    
    # Path untuk logout pengguna
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('dashboardadmin/', views.dashboardadmin, name='dashboardadmin'),
    path('admincourse/', views.admincourse, name='admincourse'),
    path('editcourse/<int:course_id>/', editcourse, name='editcourse'),
    path('dashboardcourse/<int:course_id>/', views.dashboardcourse, name='dashboardcourse'),
    path('dashboardcontent/<int:course_id>/', views.dashboardcontent, name='dashboardcontent'),

  
]

# Menambahkan URL untuk menyajikan file media selama pengembangan
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


