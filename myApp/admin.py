from django.contrib import admin
from .models import Group,Users,LanID

# Register your models here.
class GroupAdmin(admin.ModelAdmin):
    list_display = ('GRP_NM','GRP_STUS')

class UsersAdmin(admin.ModelAdmin):
    list_display = ('FRST_NM','LST_NM','UESR_STUS','GRP_ID')

class LanIDAdmin(admin.ModelAdmin):
    list_display = ('BP_LANID',)

admin.site.register(Group,GroupAdmin)
admin.site.register(Users,UsersAdmin)
admin.site.register(LanID,LanIDAdmin)