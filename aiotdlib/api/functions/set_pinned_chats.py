# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    ChatList,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SetPinnedChats(BaseObject):
    """
    Changes the order of pinned chats

    :param chat_list: Chat list in which to change the order of pinned chats
    :type chat_list: :class:`ChatList`
    :param chat_ids: The new list of pinned chats
    :type chat_ids: :class:`Vector[Int53]`
    """

    ID: typing.Literal["setPinnedChats"] = field(default="setPinnedChats", metadata={"alias": "@type"})
    chat_list: ChatList
    chat_ids: Vector[Int53]
