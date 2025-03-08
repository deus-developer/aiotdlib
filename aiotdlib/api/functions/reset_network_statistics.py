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
class ResetNetworkStatistics(BaseObject):
    """
    Resets all network data usage statistics to zero. Can be called before authorization
    """

    ID: typing.Literal["resetNetworkStatistics"] = field(default="resetNetworkStatistics", metadata={"alias": "@type"})
