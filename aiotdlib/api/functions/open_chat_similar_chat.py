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
class OpenChatSimilarChat(BaseObject):
    """
    Informs TDLib that a chat was opened from the list of similar chats. The method is independent of openChat and closeChat methods

    :param chat_id: Identifier of the original chat, which similar chats were requested
    :type chat_id: :class:`Int53`
    :param opened_chat_id: Identifier of the opened chat
    :type opened_chat_id: :class:`Int53`
    """

    ID: typing.Literal["openChatSimilarChat"] = field(default="openChatSimilarChat", metadata={"alias": "@type"})
    chat_id: Int53
    opened_chat_id: Int53
