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
class RemoveRecentlyFoundChat(BaseObject):
    """
    Removes a chat from the list of recently found chats

    :param chat_id: Identifier of the chat to be removed
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["removeRecentlyFoundChat"] = field(
        default="removeRecentlyFoundChat", metadata={"alias": "@type"}
    )
    chat_id: Int53
