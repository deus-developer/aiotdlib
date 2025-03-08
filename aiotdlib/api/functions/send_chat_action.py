# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    ChatAction,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SendChatAction(BaseObject):
    """
    Sends a notification about user activity in a chat

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param business_connection_id: Unique identifier of business connection on behalf of which to send the request; for bots only
    :type business_connection_id: :class:`String`
    :param message_thread_id: If not 0, the message thread identifier in which the action was performed
    :type message_thread_id: :class:`Int53`
    :param action: The action description; pass null to cancel the currently active action, defaults to None
    :type action: :class:`ChatAction`, optional
    """

    ID: typing.Literal["sendChatAction"] = field(default="sendChatAction", metadata={"alias": "@type"})
    chat_id: Int53
    business_connection_id: String
    message_thread_id: Int53 = field(default=0)
    action: typing.Optional[ChatAction] = field(default=None)
