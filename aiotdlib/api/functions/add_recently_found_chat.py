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
class AddRecentlyFoundChat(BaseObject):
    """
    Adds a chat to the list of recently found chats. The chat is added to the beginning of the list. If the chat is already in the list, it will be removed from the list first

    :param chat_id: Identifier of the chat to add
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["addRecentlyFoundChat"] = field(default="addRecentlyFoundChat", metadata={"alias": "@type"})
    chat_id: Int53
