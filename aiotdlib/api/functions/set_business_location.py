# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    BusinessLocation,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SetBusinessLocation(BaseObject):
    """
    Changes the business location of the current user. Requires Telegram Business subscription

    :param location: The new location of the business; pass null to remove the location, defaults to None
    :type location: :class:`BusinessLocation`, optional
    """

    ID: typing.Literal["setBusinessLocation"] = field(default="setBusinessLocation", metadata={"alias": "@type"})
    location: typing.Optional[BusinessLocation] = field(default=None)
