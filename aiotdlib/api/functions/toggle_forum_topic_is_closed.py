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
class ToggleForumTopicIsClosed(BaseObject):
    """
    Toggles whether a topic is closed in a forum supergroup chat; requires can_manage_topics right in the supergroup unless the user is creator of the topic

    :param chat_id: Identifier of the chat
    :type chat_id: :class:`Int53`
    :param message_thread_id: Message thread identifier of the forum topic
    :type message_thread_id: :class:`Int53`
    :param is_closed: Pass true to close the topic; pass false to reopen it
    :type is_closed: :class:`Bool`
    """

    ID: typing.Literal["toggleForumTopicIsClosed"] = field(
        default="toggleForumTopicIsClosed", metadata={"alias": "@type"}
    )
    chat_id: Int53
    message_thread_id: Int53
    is_closed: Bool = field(default=False)
