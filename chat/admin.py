from django.contrib import admin

from chat.models import Message, Thread


@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    pass


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass
