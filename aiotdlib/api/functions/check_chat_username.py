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
class CheckChatUsername(BaseObject):
    """
    Checks whether a username can be set for a chat

    :param username: Username to be checked
    :type username: :class:`String`
    :param chat_id: Chat identifier; must be identifier of a supergroup chat, or a channel chat, or a private chat with self, or 0 if the chat is being created
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["checkChatUsername"] = field(default="checkChatUsername", metadata={"alias": "@type"})
    username: String
    chat_id: Int53 = field(default=0)
