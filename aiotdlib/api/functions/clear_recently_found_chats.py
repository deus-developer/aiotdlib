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
class ClearRecentlyFoundChats(BaseObject):
    """
    Clears the list of recently found chats
    """

    ID: typing.Literal["clearRecentlyFoundChats"] = field(
        default="clearRecentlyFoundChats", metadata={"alias": "@type"}
    )
