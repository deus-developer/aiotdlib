# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    PremiumLimitType,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class GetPremiumLimit(BaseObject):
    """
    Returns information about a limit, increased for Premium users. Returns a 404 error if the limit is unknown

    :param limit_type: Type of the limit
    :type limit_type: :class:`PremiumLimitType`
    """

    ID: typing.Literal["getPremiumLimit"] = field(default="getPremiumLimit", metadata={"alias": "@type"})
    limit_type: PremiumLimitType
