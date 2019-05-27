from django.contrib import admin

# Register your models here.
from home.models import home_student_record,home_teacher_record,uploaded_files,course

admin.site.register(home_student_record)
admin.site.register(home_teacher_record)
admin.site.register(uploaded_files)
admin.site.register(course)