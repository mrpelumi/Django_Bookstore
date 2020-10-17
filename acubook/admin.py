from django.contrib import admin
from acubook.models import UserProfileInfo,BookInfo,Category

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(BookInfo)
admin.site.register(Category)
