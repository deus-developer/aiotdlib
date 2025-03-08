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
class GetChatBoostLink(BaseObject):
    """
    Returns an HTTPS link to boost the specified supergroup or channel chat

    :param chat_id: Identifier of the chat
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["getChatBoostLink"] = field(default="getChatBoostLink", metadata={"alias": "@type"})
    chat_id: Int53
