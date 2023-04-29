from django.contrib import admin
# Register your models here.
from blog.models import dform,contact,customer


admin.site.register(dform)
admin.site.register(contact)
admin.site.register(customer)