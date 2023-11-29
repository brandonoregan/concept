from django.urls import path
from . import views

urlpatterns = [
    path("", views.inbox, name="inbox"),
    path("create_message", views.CreateMessage.as_view(), name="create_message"),
    path("unopened/<int:message_id>/", views.unopened, name="unopened"),
]
