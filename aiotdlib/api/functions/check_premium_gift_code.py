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
class CheckPremiumGiftCode(BaseObject):
    """
    Return information about a Telegram Premium gift code

    :param code: The code to check
    :type code: :class:`String`
    """

    ID: typing.Literal["checkPremiumGiftCode"] = field(default="checkPremiumGiftCode", metadata={"alias": "@type"})
    code: String
