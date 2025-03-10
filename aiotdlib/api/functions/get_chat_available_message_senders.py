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
class GetChatAvailableMessageSenders(BaseObject):
    """
    Returns the list of message sender identifiers, which can be used to send messages in a chat

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["getChatAvailableMessageSenders"] = field(
        default="getChatAvailableMessageSenders", metadata={"alias": "@type"}
    )
    chat_id: Int53
