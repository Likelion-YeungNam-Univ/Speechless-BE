from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import Notification, Review, Message

class CustomUserAdmin(UserAdmin):
    list_display = ('user_id', 'user_name', 'email', 'id', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ( 'user_name', 'email', 'id', 'password')}),
        ('Personal Info', {'fields': ('prof_img', 'prof_intro')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'level', 'exp')}),
        ('Important Dates', {'fields': ('last_login', 'created_date')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_name', 'email', 'id', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('user_id', 'user_name', 'email', 'id')
    ordering = ('user_id',)
    filter_horizontal = ()

#공지사항
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('notice_id', 'user_id', 'title', 'is_checked')
    search_fields = ['title']
    list_filter = ('is_checked',)

#리뷰
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review_id', 'user_id', 'content')
    search_fields = ['content']

#register
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Message)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(Review, ReviewAdmin)
