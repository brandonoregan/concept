from django.db.models import Max
from .models import Conversation


def get_user_conversations(user):
    """
    Returns all user converstions in most recent order
    """
    return (
            Conversation.objects.filter(participants=user)
            .annotate(last_message_time=Max('messages__sent_at'))
            .order_by('-last_message_time')
        )


def get_unique_participants(conversations, user):
    """
    Returns a list of unique  participants from each conversation excluding user
    """
    # List for all other participants in each conversation
    other_participants_list = []
    
    for conversation in conversations:
        # Exclude the current_user to get the other participant(s)
        other_participant = conversation.participants.exclude(id=user.id)
        # Add the other participant(s) to the list
        other_participants_list.extend(other_participant)

    # Remove duplicates from the list, keeping unique participants
    unique_participants = list(set(other_participants_list))

    return unique_participants