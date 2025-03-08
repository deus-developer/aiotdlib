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
class GetSuitablePersonalChats(BaseObject):
    """
    Returns a list of channel chats, which can be used as a personal chat
    """

    ID: typing.Literal["getSuitablePersonalChats"] = field(
        default="getSuitablePersonalChats", metadata={"alias": "@type"}
    )
