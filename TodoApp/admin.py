from django.contrib import admin

from .models import Profile, Task, ChatMessage

class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'reciever', 'message', 'is_read', 'timestamp')
    list_filter = ('is_read', 'timestamp')
    is_editable = ['is_read']
    search_fields = ('sender__username', 'reciever__username', 'message')

admin.site.register(Profile)
admin.site.register(Task)
admin.site.register(ChatMessage,ChatMessageAdmin)

