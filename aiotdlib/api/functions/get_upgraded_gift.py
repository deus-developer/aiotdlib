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
class GetUpgradedGift(BaseObject):
    """
    Returns information about an upgraded gift by its name

    :param name: Unique name of the upgraded gift
    :type name: :class:`String`
    """

    ID: typing.Literal["getUpgradedGift"] = field(default="getUpgradedGift", metadata={"alias": "@type"})
    name: String
