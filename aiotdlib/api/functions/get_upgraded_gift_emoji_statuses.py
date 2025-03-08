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
class GetUpgradedGiftEmojiStatuses(BaseObject):
    """
    Returns available upgraded gift emoji statuses for self status
    """

    ID: typing.Literal["getUpgradedGiftEmojiStatuses"] = field(
        default="getUpgradedGiftEmojiStatuses", metadata={"alias": "@type"}
    )
