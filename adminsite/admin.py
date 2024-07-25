from django.contrib import admin
from .models import Course, Instructor, Lesson, Learner, Question, Choice, Enrollment, Submission

# Register your models here.
class LessonInline(admin.StackedInline):
    model = Lesson 
    extra = 5
class CourseAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'name', 'description']
    inlines = [LessonInline]
admin.site.register(Course, CourseAdmin)
admin.site.register(Instructor,)
admin.site.register(Lesson)
admin.site.register(Learner)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Enrollment)
admin.site.register(Submission)