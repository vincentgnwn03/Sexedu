from django.contrib import admin  # type: ignore
from sexeduapp.models import Laporan, UserProfileInfo

from .models import Course

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Laporan)
admin.site.register(Course)

