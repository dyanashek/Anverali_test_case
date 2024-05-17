from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import CustomerProfile, FreelancerProfile


User = get_user_model()


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'first_name', 'last_name', 'email', 'sex', 'phone', 'role',)
    empty_value_display = '-нет ответа-'
    search_fields = ('username',) 
    list_filter = ('role',) 


@admin.register(FreelancerProfile)
class FreelancerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialization',)
    empty_value_display = '-нет ответа-'


@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'currency',)
    empty_value_display = '-нет ответа-'
