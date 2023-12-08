from django.urls import path
from . import views

urlpatterns = [
    path("inbox", views.inbox, name="inbox"),
    path("inbox/<str:user_username>/", views.inbox, name="inbox_with_user"),
    path("reply_message", views.replyMessage, name="reply_message"),
    path("unopened/<int:message_id>/", views.unopened, name="unopened"),
]
