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
class SetChatDescription(BaseObject):
    """
    Changes information about a chat. Available for basic groups, supergroups, and channels. Requires can_change_info member right

    :param chat_id: Identifier of the chat
    :type chat_id: :class:`Int53`
    :param description: New chat description; 0-255 characters
    :type description: :class:`String`
    """

    ID: typing.Literal["setChatDescription"] = field(default="setChatDescription", metadata={"alias": "@type"})
    chat_id: Int53
    description: String = field(default="", metadata={"max_length": 255})
