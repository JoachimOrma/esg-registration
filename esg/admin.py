from django.contrib import admin
from .models import Mentor, Mentee

# Register your models here.
@admin.register(Mentee)
class MenteeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'career_path', 'desired_skill', 'created_at']
    search_fields = ['first_name', 'last_name']
    
@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'current_position', 'areas_of_expertise', 'created_at']
    search_fields = ['first_name', 'last_name']