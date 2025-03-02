from django.contrib import admin
from .models import Book
from .models import CustomUser

class Bookadmin(admin.ModelAdmin) :
    list_filter = ("title","author","publication_year")
    search_fields = ("title","author","publication_year")
class CustomUserAdmin(admin.ModelAdmin):
    ...

    
# Register your models here.
admin.site.register(Book,Bookadmin)
admin.site.register(CustomUser,CustomUserAdmin)


