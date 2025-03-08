# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.base import *


@dataclass(slots=True, kw_only=True)
class DeleteForumTopic(BaseObject):
    """
    Deletes all messages in a forum topic; requires can_delete_messages administrator right in the supergroup unless the user is creator of the topic, the topic has no messages from other users and has at most 11 messages

    :param chat_id: Identifier of the chat
    :type chat_id: :class:`Int53`
    :param message_thread_id: Message thread identifier of the forum topic
    :type message_thread_id: :class:`Int53`
    """

    ID: typing.Literal["deleteForumTopic"] = field(default="deleteForumTopic", metadata={"alias": "@type"})
    chat_id: Int53
    message_thread_id: Int53
