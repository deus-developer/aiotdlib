# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    PremiumFeature,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class ViewPremiumFeature(BaseObject):
    """
    Informs TDLib that the user viewed detailed information about a Premium feature on the Premium features screen

    :param feature: The viewed premium feature
    :type feature: :class:`PremiumFeature`
    """

    ID: typing.Literal["viewPremiumFeature"] = field(default="viewPremiumFeature", metadata={"alias": "@type"})
    feature: PremiumFeature
