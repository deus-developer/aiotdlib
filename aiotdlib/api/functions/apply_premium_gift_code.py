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
class ApplyPremiumGiftCode(BaseObject):
    """
    Applies a Telegram Premium gift code

    :param code: The code to apply
    :type code: :class:`String`
    """

    ID: typing.Literal["applyPremiumGiftCode"] = field(default="applyPremiumGiftCode", metadata={"alias": "@type"})
    code: String
