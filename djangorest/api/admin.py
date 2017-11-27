from django.contrib import admin

from .models import Bucketlist, Item

admin.site.site_header = "Bucketlist Administration"
admin.site.site_title = "Bucketlist Administration"

# Register your models here.
admin.site.register(Bucketlist)
admin.site.register(Item)