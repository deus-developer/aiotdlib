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
class GetRecentInlineBots(BaseObject):
    """
    Returns up to 20 recently used inline bots in the order of their last usage
    """

    ID: typing.Literal["getRecentInlineBots"] = field(default="getRecentInlineBots", metadata={"alias": "@type"})
