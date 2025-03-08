# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    MessageSender,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SetChatMessageSender(BaseObject):
    """
    Selects a message sender to send messages in a chat

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param message_sender_id: New message sender for the chat
    :type message_sender_id: :class:`MessageSender`
    """

    ID: typing.Literal["setChatMessageSender"] = field(default="setChatMessageSender", metadata={"alias": "@type"})
    chat_id: Int53
    message_sender_id: MessageSender
