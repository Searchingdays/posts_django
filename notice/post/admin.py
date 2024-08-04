from django.contrib import admin

from .models import msg, comment

# Register your models here.

#admin.site.register(msg)
admin.site.register(comment)

class msg_new(admin.ModelAdmin):
    fields= ["msg_title","msg_date", "msg_text"]
    #fieldsets = [[None,"msg_title"],("Date",{"fields":["msg_date"]}), [None,"msg_text"] ]

admin.site.register(msg, msg_new)




