from django.contrib import admin
from isthiskeanureeves.models import Category, Page
from isthiskeanureeves.models import UserProfile

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page)
admin.site.register(UserProfile)

