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
class SetPersonalChat(BaseObject):
    """
    Changes the personal chat of the current user

    :param chat_id: Identifier of the new personal chat; pass 0 to remove the chat. Use getSuitablePersonalChats to get suitable chats
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["setPersonalChat"] = field(default="setPersonalChat", metadata={"alias": "@type"})
    chat_id: Int53
