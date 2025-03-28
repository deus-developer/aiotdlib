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
class GetPremiumStickerExamples(BaseObject):
    """
    Returns examples of premium stickers for demonstration purposes
    """

    ID: typing.Literal["getPremiumStickerExamples"] = field(
        default="getPremiumStickerExamples", metadata={"alias": "@type"}
    )
