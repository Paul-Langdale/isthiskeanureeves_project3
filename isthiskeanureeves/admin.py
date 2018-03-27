from django.contrib import admin
from isthiskeanureeves.models import Category, Page
from isthiskeanureeves.models import UserProfile


#Category and Page class to the admin interface

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}



class PageAdmin(admin.ModelAdmin):
    list_display =('title', 'category', 'rating')
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)

