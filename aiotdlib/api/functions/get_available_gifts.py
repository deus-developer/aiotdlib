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
class GetAvailableGifts(BaseObject):
    """
    Returns gifts that can be sent to other users and channel chats
    """

    ID: typing.Literal["getAvailableGifts"] = field(default="getAvailableGifts", metadata={"alias": "@type"})
