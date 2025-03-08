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
class GetOwnedBots(BaseObject):
    """
    Returns the list of bots owned by the current user
    """

    ID: typing.Literal["getOwnedBots"] = field(default="getOwnedBots", metadata={"alias": "@type"})
