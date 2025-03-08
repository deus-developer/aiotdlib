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
class GetChatBoostStatus(BaseObject):
    """
    Returns the current boost status for a supergroup or a channel chat

    :param chat_id: Identifier of the chat
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["getChatBoostStatus"] = field(default="getChatBoostStatus", metadata={"alias": "@type"})
    chat_id: Int53
