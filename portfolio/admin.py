from django.contrib import admin
from .models import (
    WhatIDo, MySkill,
    MyExperience, MyWork,
    MyEducation, MyWorkingExperiences,
)


admin.site.register(WhatIDo)
admin.site.register(MySkill)
admin.site.register(MyExperience)
admin.site.register(MyWork)
admin.site.register(MyEducation)
admin.site.register(MyWorkingExperiences)
