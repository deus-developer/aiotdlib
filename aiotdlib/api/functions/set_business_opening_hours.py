# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    BusinessOpeningHours,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SetBusinessOpeningHours(BaseObject):
    """
    Changes the business opening hours of the current user. Requires Telegram Business subscription

    :param opening_hours: The new opening hours of the business; pass null to remove the opening hours; up to 28 time intervals can be specified, defaults to None
    :type opening_hours: :class:`BusinessOpeningHours`, optional
    """

    ID: typing.Literal["setBusinessOpeningHours"] = field(
        default="setBusinessOpeningHours", metadata={"alias": "@type"}
    )
    opening_hours: typing.Optional[BusinessOpeningHours] = field(default=None)
