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
class GetNetworkStatistics(BaseObject):
    """
    Returns network data usage statistics. Can be called before authorization

    :param only_current: Pass true to get statistics only for the current library launch
    :type only_current: :class:`Bool`
    """

    ID: typing.Literal["getNetworkStatistics"] = field(default="getNetworkStatistics", metadata={"alias": "@type"})
    only_current: Bool = field(default=False)
