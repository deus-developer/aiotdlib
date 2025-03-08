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
class ClickPremiumSubscriptionButton(BaseObject):
    """
    Informs TDLib that the user clicked Premium subscription button on the Premium features screen
    """

    ID: typing.Literal["clickPremiumSubscriptionButton"] = field(
        default="clickPremiumSubscriptionButton", metadata={"alias": "@type"}
    )
