# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    MessageSender,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class GetStarRevenueStatistics(BaseObject):
    """
    Returns detailed Telegram Star revenue statistics

    :param owner_id: Identifier of the owner of the Telegram Stars; can be identifier of an owned bot, or identifier of a channel chat with supergroupFullInfo.can_get_star_revenue_statistics == true
    :type owner_id: :class:`MessageSender`
    :param is_dark: Pass true if a dark theme is used by the application
    :type is_dark: :class:`Bool`
    """

    ID: typing.Literal["getStarRevenueStatistics"] = field(
        default="getStarRevenueStatistics", metadata={"alias": "@type"}
    )
    owner_id: MessageSender
    is_dark: Bool = field(default=False)
