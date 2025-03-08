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
class GetStarGiftPaymentOptions(BaseObject):
    """
    Returns available options for Telegram Stars gifting

    :param user_id: Identifier of the user that will receive Telegram Stars; pass 0 to get options for an unspecified user
    :type user_id: :class:`Int53`
    """

    ID: typing.Literal["getStarGiftPaymentOptions"] = field(
        default="getStarGiftPaymentOptions", metadata={"alias": "@type"}
    )
    user_id: Int53
