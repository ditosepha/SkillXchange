from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(SkillClass)
admin.site.register(Enrollment)
admin.site.register(Review)