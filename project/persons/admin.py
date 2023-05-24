from django.contrib import admin
from persons.models import Department, Person, Course,Purpose

# Register your models here.


admin.site.register(Course)
admin.site.register(Department)
admin.site.register(Purpose)
admin.site.register(Person)

