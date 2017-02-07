from django.contrib import admin
from author.models import Profile
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = 'id family avatar'.split()
    list_editable = 'family'.split()

admin.site.register(Profile,ProfileAdmin)
