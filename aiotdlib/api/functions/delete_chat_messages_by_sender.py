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
class DeleteChatMessagesBySender(BaseObject):
    """
    Deletes all messages sent by the specified message sender in a chat. Supported only for supergroups; requires can_delete_messages administrator right

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param sender_id: Identifier of the sender of messages to delete
    :type sender_id: :class:`MessageSender`
    """

    ID: typing.Literal["deleteChatMessagesBySender"] = field(
        default="deleteChatMessagesBySender", metadata={"alias": "@type"}
    )
    chat_id: Int53
    sender_id: MessageSender
