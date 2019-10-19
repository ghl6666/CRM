from django.contrib import admin
from nbapp import models

# Register your models here.
from nbapp import models

class PermissonAdmin(admin.ModelAdmin):
    list_display = ['pk','title','url']


class RoleAdmin(admin.ModelAdmin):
    list_display = ['pk','title',]



admin.site.register(models.UserInfo)
admin.site.register(models.Role,RoleAdmin)
admin.site.register(models.Permission,PermissonAdmin)

# admin.site.register(models.Customer)
# admin.site.register(models.Campuses)
admin.site.register(models.ClassList)
admin.site.register(models.StudentStudyRecord)
admin.site.register(models.ClassStudyRecord)
admin.site.register(models.Student)




