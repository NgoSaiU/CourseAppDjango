from django.contrib import admin

# Register your models here.
# Dang ky model

from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Courses, Lesson, Tag
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['id', 'name']

class CourseForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Courses
        fields = '__all__'

class  TagInlineAdmin(admin.StackedInline):
    model = Courses.tags.through
class CourseAdmin(admin.ModelAdmin):
    readonly_fields = ['img']
    inlines =  [TagInlineAdmin]
    form = CourseForm
    def img(self, course):
        if course:
            return mark_safe(
                '<img src = "/static/{url}/" width = "120" />'\
                    .format(url=course.image.name)
            )

    class Media:
        css = {
            'all': ('/static/css/style.css',)
        }

admin.site.register(Category,CategoryAdmin)
admin.site.register(Courses, CourseAdmin)
admin.site.register(Lesson)
admin.site.register(Tag)
