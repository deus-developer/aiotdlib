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
class ClearRecentReactions(BaseObject):
    """
    Clears the list of recently used reactions
    """

    ID: typing.Literal["clearRecentReactions"] = field(default="clearRecentReactions", metadata={"alias": "@type"})
