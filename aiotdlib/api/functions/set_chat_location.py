# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    ChatLocation,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SetChatLocation(BaseObject):
    """
    Changes the location of a chat. Available only for some location-based supergroups, use supergroupFullInfo.can_set_location to check whether the method is allowed to use

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param location: New location for the chat; must be valid and not null
    :type location: :class:`ChatLocation`
    """

    ID: typing.Literal["setChatLocation"] = field(default="setChatLocation", metadata={"alias": "@type"})
    chat_id: Int53
    location: ChatLocation
