# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    PremiumSource,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class GetPremiumFeatures(BaseObject):
    """
    Returns information about features, available to Premium users

    :param source: Source of the request; pass null if the method is called from some non-standard source, defaults to None
    :type source: :class:`PremiumSource`, optional
    """

    ID: typing.Literal["getPremiumFeatures"] = field(default="getPremiumFeatures", metadata={"alias": "@type"})
    source: typing.Optional[PremiumSource] = field(default=None)
