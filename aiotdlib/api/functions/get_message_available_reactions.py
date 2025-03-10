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
class GetMessageAvailableReactions(BaseObject):
    """
    Returns reactions, which can be added to a message. The list can change after updateActiveEmojiReactions, updateChatAvailableReactions for the chat, or updateMessageInteractionInfo for the message

    :param chat_id: Identifier of the chat to which the message belongs
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message
    :type message_id: :class:`Int53`
    :param row_size: Number of reaction per row, 5-25
    :type row_size: :class:`Int32`
    """

    ID: typing.Literal["getMessageAvailableReactions"] = field(
        default="getMessageAvailableReactions", metadata={"alias": "@type"}
    )
    chat_id: Int53
    message_id: Int53
    row_size: Int32
