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
class GetStarPaymentOptions(BaseObject):
    """
    Returns available options for Telegram Stars purchase
    """

    ID: typing.Literal["getStarPaymentOptions"] = field(default="getStarPaymentOptions", metadata={"alias": "@type"})
