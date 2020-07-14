from django.contrib import admin
from .models import Blog
from django_summernote.admin import SummernoteModelAdmin

from.models.SomeModel import SomeModel

import numba



class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    summernote_fields = ('content',)



class SomeModelAdmin(admin.ModelAdmin):
    model = SomeModel


    admin.site.register(admin, PostAdmin)


    admin.site.register(SomeModel, SomeModelAdmin)



class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


admin.site.register(SomeModelAdmin, SomeModel)

admin.site.register(Blog, PostAdmin)
