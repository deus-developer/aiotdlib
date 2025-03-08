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
class GetStarGiveawayPaymentOptions(BaseObject):
    """
    Returns available options for Telegram Star giveaway creation
    """

    ID: typing.Literal["getStarGiveawayPaymentOptions"] = field(
        default="getStarGiveawayPaymentOptions", metadata={"alias": "@type"}
    )
