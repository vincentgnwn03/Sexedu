from django.contrib.auth import authenticate  # type: ignore
from django.contrib.auth import logout  # type: ignore
from django.contrib.auth import login
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required  # type: ignore
from django.contrib.auth.models import User  # type: ignore
from django.http import HttpResponse, HttpResponseRedirect  # type: ignore
from django.shortcuts import (  # type: ignore; type: ignore # Import get_object_or_404
    get_object_or_404, redirect, render)
from django.urls import reverse  # type: ignore
from django.utils import timezone  # type: ignore
from sexeduapp.forms import (LaporanForm, ProfileUpdateForm, UserForm,
                             UserProfileInfoForm, UserUpdateForm)
from sexeduapp.models import Course, Laporan, Profile

from .models import Course


def index(request):
    return render(request, 'sexeduapp/index.html')


def course(request):
    return render(request, 'sexeduapp/course.html')


def report(request):
    if request.method == 'POST':
        nama = request.POST.get('nama')
        email = request.POST.get('email')
        deskripsi = request.POST.get('deskripsi')

        laporan_baru = Laporan(nama=nama, email=email, deskripsi=deskripsi, waktu_laporan=timezone.now())
        laporan_baru.save()

        return HttpResponseRedirect(reverse('sexeduapp:pesanberhasil'))

    return render(request, "sexeduapp/report.html")


@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return HttpResponse("Account not active")
        else:
            print("Login failed")
    return render(request, 'login.html')

from django.contrib.auth.models import User
from django.shortcuts import HttpResponse, redirect, render

from .forms import UserForm, UserProfileInfoForm
from .models import Profile


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']

            # Check if the user already exists
            if User.objects.filter(username=username).exists():
                return HttpResponse("Username already exists. Please choose a different username.")

            # Create the user object
            user = user_form.save(commit=False)
            user.set_password(password)  # Set the password correctly
            user.save()

            # Create the profile object
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'sexeduapp/register.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    })


def class_content(request):
    return render(request, 'sexeduapp/class_content.html')


def about(request):
    return render(request, 'sexeduapp/about.html')


def login(request):
    return render(request, 'sexeduapp/login.html')


def dashboard(request):
    return render(request, 'sexeduapp/dashboard.html')


def dashboardadmin(request):
    total_courses = Course.objects.count()
    users = User.objects.filter(is_superuser=False)
    total_users = User.objects.filter(is_superuser=False).count()
    total_superusers = User.objects.filter(is_superuser=True).count()
    context = {
        'total_users': total_users,
        'total_superusers': total_superusers,
        'total_courses': total_courses,
        'users': users
    }
    return render(request, 'sexeduapp/dashboardadmin.html', context)


def admincourse(request):
    courses = Course.objects.all()
    return render(request, 'sexeduapp/admincourse.html', {'courses': courses})


def dashboardcourse(request):
    user_courses = request.user.courses.all()
    context = {
        'courses': user_courses,
    }
    return render(request, 'sexeduapp/dashboardcourse.html', context)


def editcourse(request, course_id):
    course = get_object_or_404(Course, pk=course_id) # type: ignore
    users = User.objects.filter(is_superuser=False)
    print(users)
    context = {
        'users': users,
        'course': course,
    }
    return render(request, 'sexeduapp/editcourse.html', context)


def pesanberhasil(request):
    return render(request, 'sexeduapp/pesanberhasil.html')


def report_view(request):
    if request.method == 'POST':
        form = LaporanForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('sexeduapp:pesanberhasil'))
    else:
        form = LaporanForm()

    return render(request, 'sexeduapp/report.html', {'form': form})


def pesanberhasil_view(request):
    return render(request, 'sexeduapp/pesanberhasil.html')


@login_required
def profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'sexeduapp/profile.html', context)


@login_required
def editcourse(request, course_id):
    course = get_object_or_404(Course, id=course_id) # type: ignore

    if request.method == 'POST':
        ppt_file = request.FILES.get('ppt')
        video_file = request.FILES.get('video')

        if ppt_file:
            course.ppt = ppt_file
        if video_file:
            course.video = video_file

        course.save()

        selected_user_id = request.POST.getlist('selected_users')
        selected_users = User.objects.filter(id__in=selected_user_id)

        course.users.clear()

        for user in selected_users:
            course.users.add(user)

        return redirect('admincourse')

    context = {
        'course': course,
        'users': User.objects.filter(is_superuser=False),
    }
    return render(request, 'sexeduapp/editcourse.html', context)


@login_required
def dashboardcontent(request, course_id):
    course = get_object_or_404(Course, id=course_id) # type: ignore
    user_courses = request.user.courses.all()
    context = {
        'courses': user_courses,
        'course': course,
    }
    return render(request, 'sexeduapp/dashboardcontent.html', context)


@login_required
def dashboardstudent(request):
    total_users = User.objects.filter(is_superuser=False).count()
    total_superusers = User.objects.filter(is_superuser=True).count()
    user_courses = request.user.courses.all()

    context = {
        'total_users': total_users,
        'total_superusers': total_superusers,
        'user': request.user,
        'user_courses': user_courses,
    }
    return render(request, 'sexeduapp/dashboardstudent.html', context)
