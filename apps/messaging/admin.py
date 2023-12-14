from django.contrib import admin
from apps.messaging.models import Conversation, Message


class ConversationAdmin(admin.ModelAdmin):
    pass


class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "sender",
        "receiver",
        "sent_at",
    )


admin.site.register(Conversation, ConversationAdmin)
admin.site.register(Message, MessageAdmin)
