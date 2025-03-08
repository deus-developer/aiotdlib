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
class UnpinChatMessage(BaseObject):
    """
    Removes a pinned message from a chat; requires can_pin_messages member right if the chat is a basic group or supergroup, or can_edit_messages administrator right if the chat is a channel

    :param chat_id: Identifier of the chat
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the removed pinned message
    :type message_id: :class:`Int53`
    """

    ID: typing.Literal["unpinChatMessage"] = field(default="unpinChatMessage", metadata={"alias": "@type"})
    chat_id: Int53
    message_id: Int53
