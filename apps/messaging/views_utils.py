from django.db.models import Max
from .models import Conversation, Message
from django.db.models import Q
from collections import OrderedDict
from datetime import datetime


def get_user_conversations(user):
    """
    Returns all user converstions in most recent order
    """
    return (
        Conversation.objects.filter(participants=user)
        .annotate(last_message_time=Max("messages__sent_at"))
        .order_by("-last_message_time")
    )


def get_unique_participants(conversations, user):
    """
    Returns a list of unique  participants from each conversation
    excluding user
    """

    other_participants_list = []

    for conversation in conversations:
        other_participant = conversation.participants.exclude(id=user.id)

        other_participants_list.extend(other_participant)

    unique_participants = list(set(other_participants_list))

    return unique_participants


def get_conversation_message_history(user1, user2):
    """
    Retrieve conversation messages between two users
    """
    return Message.objects.filter(
        Q(sender=user1, receiver=user2) | Q(sender=user2, receiver=user1)
    ).order_by("sent_at")


def get_recent_messages(current_user, unique_participants):
    """
    Returns a dictionary of the unique users and the last message
    between the current_user, ordered by last message sent
    """
    unordered_dict = {}

    for participant in unique_participants:
        conversation = get_conversation_message_history(
            current_user, participant
        )

        # Fetch the last message in the conversation if it exists
        last_message = conversation.last() if conversation.exists() else None

        unordered_dict[participant] = last_message

    ordered_dict = OrderedDict(
        sorted(
            unordered_dict.items(),
            key=lambda x: x[1].sent_at if x[1] else None,
            reverse=True,
        )
    )

    return ordered_dict


def format_last_login(last_login):
    """
    Format the last_login time
    """
    now = datetime.utcnow().replace(tzinfo=None)
    last_login_naive = last_login.replace(tzinfo=None)

    time_diff = now - last_login_naive
    hours = max(int(time_diff.total_seconds() / 3600), 1)

    if time_diff.total_seconds() < 3600:
        return "1 hour ago"

    elif 3600 <= time_diff.total_seconds() < 86400:
        return f"{hours} hour{'s' if hours > 1 else ''} ago"

    else:
        days = time_diff.days
        return f"{days} day{'s' if days > 1 else ''} ago"
