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
class GetDefaultProfilePhotoCustomEmojiStickers(BaseObject):
    """
    Returns default list of custom emoji stickers for placing on a profile photo
    """

    ID: typing.Literal["getDefaultProfilePhotoCustomEmojiStickers"] = field(
        default="getDefaultProfilePhotoCustomEmojiStickers", metadata={"alias": "@type"}
    )
