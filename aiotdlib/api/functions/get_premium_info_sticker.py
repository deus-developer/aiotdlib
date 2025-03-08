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
class GetPremiumInfoSticker(BaseObject):
    """
    Returns the sticker to be used as representation of the Telegram Premium subscription

    :param month_count: Number of months the Telegram Premium subscription will be active
    :type month_count: :class:`Int32`
    """

    ID: typing.Literal["getPremiumInfoSticker"] = field(default="getPremiumInfoSticker", metadata={"alias": "@type"})
    month_count: Int32
