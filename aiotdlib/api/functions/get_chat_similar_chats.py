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
class GetChatSimilarChats(BaseObject):
    """
    Returns a list of chats similar to the given chat

    :param chat_id: Identifier of the target chat; must be an identifier of a channel chat
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["getChatSimilarChats"] = field(default="getChatSimilarChats", metadata={"alias": "@type"})
    chat_id: Int53
