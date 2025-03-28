# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    InputFile,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class AddFavoriteSticker(BaseObject):
    """
    Adds a new sticker to the list of favorite stickers. The new sticker is added to the top of the list. If the sticker was already in the list, it is removed from the list first. Only stickers belonging to a sticker set or in WEBP or WEBM format can be added to this list. Emoji stickers can't be added to favorite stickers

    :param sticker: Sticker file to add
    :type sticker: :class:`InputFile`
    """

    ID: typing.Literal["addFavoriteSticker"] = field(default="addFavoriteSticker", metadata={"alias": "@type"})
    sticker: InputFile
