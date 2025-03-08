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
class GetGreetingStickers(BaseObject):
    """
    Returns greeting stickers from regular sticker sets that can be used for the start page of other users
    """

    ID: typing.Literal["getGreetingStickers"] = field(default="getGreetingStickers", metadata={"alias": "@type"})
