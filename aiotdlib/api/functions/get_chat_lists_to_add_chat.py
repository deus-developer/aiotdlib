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
class GetChatListsToAddChat(BaseObject):
    """
    Returns chat lists to which the chat can be added. This is an offline request

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["getChatListsToAddChat"] = field(default="getChatListsToAddChat", metadata={"alias": "@type"})
    chat_id: Int53
