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
class GetRecentlyOpenedChats(BaseObject):
    """
    Returns recently opened chats; this is an offline request. Returns chats in the order of last opening

    :param limit: The maximum number of chats to be returned
    :type limit: :class:`Int32`
    """

    ID: typing.Literal["getRecentlyOpenedChats"] = field(default="getRecentlyOpenedChats", metadata={"alias": "@type"})
    limit: Int32
