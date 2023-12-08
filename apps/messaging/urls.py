from django.urls import path
from . import views

urlpatterns = [
    path("", views.inbox, name="inbox"),
    path("reply_message", views.replyMessage, name="reply_message"),
    path("unopened/<int:message_id>/", views.unopened, name="unopened"),
]
