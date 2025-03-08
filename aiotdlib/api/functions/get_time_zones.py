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
class GetTimeZones(BaseObject):
    """
    Returns the list of supported time zones
    """

    ID: typing.Literal["getTimeZones"] = field(default="getTimeZones", metadata={"alias": "@type"})
