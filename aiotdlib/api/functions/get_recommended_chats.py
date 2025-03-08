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
class GetRecommendedChats(BaseObject):
    """
    Returns a list of channel chats recommended to the current user
    """

    ID: typing.Literal["getRecommendedChats"] = field(default="getRecommendedChats", metadata={"alias": "@type"})
