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
class GetDefaultBackgroundCustomEmojiStickers(BaseObject):
    """
    Returns default list of custom emoji stickers for reply background
    """

    ID: typing.Literal["getDefaultBackgroundCustomEmojiStickers"] = field(
        default="getDefaultBackgroundCustomEmojiStickers", metadata={"alias": "@type"}
    )
