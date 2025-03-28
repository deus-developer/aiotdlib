# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    ChatAvailableReactions,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SetChatAvailableReactions(BaseObject):
    """
    Changes reactions, available in a chat. Available for basic groups, supergroups, and channels. Requires can_change_info member right

    :param chat_id: Identifier of the chat
    :type chat_id: :class:`Int53`
    :param available_reactions: Reactions available in the chat. All explicitly specified emoji reactions must be active. In channel chats up to the chat's boost level custom emoji reactions can be explicitly specified
    :type available_reactions: :class:`ChatAvailableReactions`
    """

    ID: typing.Literal["setChatAvailableReactions"] = field(
        default="setChatAvailableReactions", metadata={"alias": "@type"}
    )
    chat_id: Int53
    available_reactions: ChatAvailableReactions
