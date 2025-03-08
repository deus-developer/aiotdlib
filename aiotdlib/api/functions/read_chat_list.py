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
class ReadChatList(BaseObject):
    """
    Traverse all chats in a chat list and marks all messages in the chats as read

    :param chat_list: Chat list in which to mark all chats as read
    :type chat_list: :class:`ChatList`
    """

    ID: typing.Literal["readChatList"] = field(default="readChatList", metadata={"alias": "@type"})
    chat_list: ChatList
