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
class GetPremiumState(BaseObject):
    """
    Returns state of Telegram Premium subscription and promotion videos for Premium features
    """

    ID: typing.Literal["getPremiumState"] = field(default="getPremiumState", metadata={"alias": "@type"})
