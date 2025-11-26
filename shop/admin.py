from django.contrib import admin
from . import models


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'price', 'category')


class CoursesInLine(admin.TabularInline):
    model = models.Course
    exclude = ['created_at']
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_of')
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Dates', {
            'fields': ['created_of'],
            'classes': ['collapse']
        })
    ]
    inlines = [CoursesInLine]


admin.site.site_title = "Courses"
admin.site.site_header = "㋛"
admin.site.index_title = "Administrator"
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Course, CourseAdmin)


