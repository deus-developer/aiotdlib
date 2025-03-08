# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    TopChatCategory,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class RemoveTopChat(BaseObject):
    """
    Removes a chat from the list of frequently used chats. Supported only if the chat info database is enabled

    :param category: Category of frequently used chats
    :type category: :class:`TopChatCategory`
    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["removeTopChat"] = field(default="removeTopChat", metadata={"alias": "@type"})
    category: TopChatCategory
    chat_id: Int53
