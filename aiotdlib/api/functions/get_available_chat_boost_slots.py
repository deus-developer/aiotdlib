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
class GetAvailableChatBoostSlots(BaseObject):
    """
    Returns the list of available chat boost slots for the current user
    """

    ID: typing.Literal["getAvailableChatBoostSlots"] = field(
        default="getAvailableChatBoostSlots", metadata={"alias": "@type"}
    )
