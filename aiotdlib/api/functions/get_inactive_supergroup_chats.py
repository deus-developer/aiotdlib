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
class GetInactiveSupergroupChats(BaseObject):
    """
    Returns a list of recently inactive supergroups and channels. Can be used when user reaches limit on the number of joined supergroups and channels and receives CHANNELS_TOO_MUCH error. Also, the limit can be increased with Telegram Premium
    """

    ID: typing.Literal["getInactiveSupergroupChats"] = field(
        default="getInactiveSupergroupChats", metadata={"alias": "@type"}
    )
